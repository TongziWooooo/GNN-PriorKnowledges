from __future__ import print_function
import numpy as np
import networkx as nx
import argparse
from sklearn.decomposition import PCA


cmd_opt = argparse.ArgumentParser(description='Argparser for graph_classification')
cmd_opt.add_argument('-mode', default='gpu', help='cpu/gpu')
cmd_opt.add_argument('-gm', default='DGCNN', help='mean_field/loopy_bp')
cmd_opt.add_argument('-data', default='DD', help='data folder name')
cmd_opt.add_argument('-batch_size', type=int, default=30, help='minibatch size')
cmd_opt.add_argument('-seed', type=int, default=1, help='seed')
cmd_opt.add_argument('-feat_dim', type=int, default=0, help='dimension of discrete node feature (maximum node tag)')
cmd_opt.add_argument('-num_class', type=int, default=0, help='#classes')
cmd_opt.add_argument('-fold', type=int, default=1, help='fold (1..10)')
cmd_opt.add_argument('-test_number', type=int, default=0, help='if specified, will overwrite -fold and use the last -test_number graphs as testing data')
cmd_opt.add_argument('-num_epochs', type=int, default=200, help='number of epochs')
cmd_opt.add_argument('-latent_dim', type=str, default='32-48-64', help='dimension(s) of latent layers')
cmd_opt.add_argument('-sortpooling_k', type=float, default=0.6, help='number of nodes kept after SortPooling')
cmd_opt.add_argument('-out_dim', type=int, default=0, help='s2v output size')
cmd_opt.add_argument('-hidden', type=int, default=128, help='dimension of regression')
cmd_opt.add_argument('-max_lv', type=int, default=4, help='max rounds of message passing')
cmd_opt.add_argument('-learning_rate', type=float, default=0.001, help='init learning_rate')
cmd_opt.add_argument('-dropout', type=bool, default=False, help='whether add dropout after dense layer')
cmd_opt.add_argument('-printAUC', type=bool, default=False, help='whether to print AUC (for binary classification only)')
cmd_opt.add_argument('-extract_features', type=bool, default=False, help='whether to extract final graph features')

cmd_args, _ = cmd_opt.parse_known_args()

cmd_args.latent_dim = [int(x) for x in cmd_args.latent_dim.split('-')]
if len(cmd_args.latent_dim) == 1:
    cmd_args.latent_dim = cmd_args.latent_dim[0]


class S2VGraph(object):
    def __init__(self, g, label, node_tags=None, node_features=None):
        '''
            g: a networkx graph
            label: an integer graph label
            node_tags: a list of integer node tags
            node_features: a numpy array of continuous node features
        '''
        self.num_nodes = len(node_tags)
        self.node_tags = node_tags
        self.label = label
        self.node_features = node_features  # numpy array (node_num * feature_dim)
        self.degs = list(dict(g.degree).values())

        if len(g.edges()) != 0:
            x, y = zip(*g.edges())
            self.num_edges = len(x)        
            self.edge_pairs = np.ndarray(shape=(self.num_edges, 2), dtype=np.int32)
            self.edge_pairs[:, 0] = x
            self.edge_pairs[:, 1] = y
            self.edge_pairs = self.edge_pairs.flatten()
        else:
            self.num_edges = 0
            self.edge_pairs = np.array([])


def load_data():
    print('loading data')
    g_list = []
    label_dict = {}
    feat_dict = {}
    prior_knowledge = []
    prior_knowledge_train = None
    prior_knowledge_test = None
    prior_knowledge_slice = None

    with open('./data/%s/%s.txt' % (cmd_args.data, cmd_args.data), 'r') as f:
        n_g = int(f.readline().strip())
        for i in range(n_g):
            row = f.readline().strip().split()
            n, l = [int(w) for w in row]
            if not l in label_dict:
                mapped = len(label_dict)
                label_dict[l] = mapped
            g = nx.Graph()
            node_tags = []
            node_features = []
            n_edges = 0
            for j in range(n):
                g.add_node(j)
                read_row = f.readline().strip().split()
                tmp = int(read_row[1]) + 2
                if tmp == len(read_row):
                    # no node attributes
                    row = [int(w) for w in read_row]
                    attr = None
                else:
                    row, attr = [int(w) for w in read_row[:tmp]], np.array([float(w) for w in read_row[tmp:]])
                if not row[0] in feat_dict:
                    mapped = len(feat_dict)
                    feat_dict[row[0]] = mapped
                node_tags.append(feat_dict[row[0]])

                if tmp < len(read_row):
                    node_features.append(attr)

                n_edges += row[1]
                for k in range(2, len(row)):
                    g.add_edge(j, row[k])

            if node_features != []:
                node_features = np.stack(node_features)
                node_feature_flag = True
            else:
                node_features = None
                node_feature_flag = False

            #assert len(g.edges()) * 2 == n_edges  (some graphs in COLLAB have self-loops, ignored here)
            assert len(g) == n
            g_list.append(S2VGraph(g, l, node_tags, node_features))
    for g in g_list:
        g.label = label_dict[g.label]
    cmd_args.num_class = len(label_dict)
    cmd_args.feat_dim = len(feat_dict)  # maximum node label (tag)
    if node_feature_flag == True:
        cmd_args.attr_dim = node_features.shape[1]  # dim of node features (attributes)
    else:
        cmd_args.attr_dim = 0

    print('# classes: %d' % cmd_args.num_class)
    print('# maximum node tag: %d' % cmd_args.feat_dim)
    print('# attr_dim: %d' % cmd_args.attr_dim)

    if cmd_args.data in ['PROTEINS_full']:
        global_info = []
        if cmd_args.data == 'PROTEINS_full':
            with open('./data/%s/%s_global_info.txt' % (cmd_args.data, cmd_args.data), 'r') as f_global_info:
                for line in f_global_info:
                    global_info.append([float(i) for i in line.strip().split()])
                print('# global info size: {}*{}'.format(len(global_info), len(global_info[0])))
            pca = PCA(n_components=0.95)
            global_info = pca.fit_transform(global_info)
            print("PCA variance ratio: ", pca.explained_variance_ratio_)
            print('# global info size after PCA: {}*{}'.format(len(global_info), len(global_info[0])))
            prior_knowledge_slice = len(global_info[0])
        else:
            prior_knowledge_slice = 0

        subgraph_info = np.load('./data/%s/%s_subgraph_info.npy' % (cmd_args.data, cmd_args.data))
        print('# subgraph info size: {}*{}'.format(len(subgraph_info), len(subgraph_info[0])))
        pca = PCA(n_components=3)
        subgraph_info = pca.fit_transform(subgraph_info)
        print("PCA variance ratio: ", pca.explained_variance_ratio_)
        print('# subgraph info size after PCA: {}*{}'.format(len(subgraph_info), len(subgraph_info[0])))

        if cmd_args.data == 'PROTEINS_full':
            prior_knowledge = np.concatenate((np.array(global_info), subgraph_info), axis=1)
        else:
            prior_knowledge = subgraph_info
        print('# prior knowledge size: {}*{}'.format(len(prior_knowledge), len(prior_knowledge[0])))

    if cmd_args.test_number == 0:
        train_idxes = np.loadtxt('./data/%s/10fold_idx/train_idx-%d.txt' % (cmd_args.data, cmd_args.fold), dtype=np.int32).tolist()
        test_idxes = np.loadtxt('./data/%s/10fold_idx/test_idx-%d.txt' % (cmd_args.data, cmd_args.fold), dtype=np.int32).tolist()
        train_graphs = [g_list[i] for i in train_idxes]
        test_graphs = [g_list[i] for i in test_idxes]
        if cmd_args.data in ['PROTEINS_full']:
            prior_knowledge_train = [prior_knowledge[i] for i in train_idxes]
            prior_knowledge_test = [prior_knowledge[i] for i in test_idxes]
    else:
        train_graphs = g_list[: n_g - cmd_args.test_number]
        test_graphs = g_list[n_g - cmd_args.test_number:]
        if cmd_args.data in ['PROTEINS_full']:
            prior_knowledge_train = prior_knowledge[: n_g - cmd_args.test_number]
            prior_knowledge_test = prior_knowledge[n_g - cmd_args.test_number:]
    return train_graphs, test_graphs, prior_knowledge_train, prior_knowledge_test, prior_knowledge_slice



