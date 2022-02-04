from torch_geometric.datasets import TUDataset
from torch_geometric.utils import to_networkx
from subgraph_matching.alignment import gen_alignment_matrix
from subgraph_matching.config import parse_encoder
from subgraph_matching.train import build_model
import networkx as nx
import argparse
import pickle
import numpy as np

dataset_name = 'proteins'
dataset = None
file_root = './neural-subgraph-learning-GNN/'

if dataset_name == 'proteins':
    dataset = TUDataset(root='/tmp/PROTEINS', name='PROTEINS')

with open(file_root + 'results/out-patterns_proteins_0.p', 'rb') as f_0, \
        open(file_root + 'results/out-patterns_proteins_1.p', 'rb') as f_1:
    subgraphs_0 = pickle.load(f_0)
    subgraphs_1 = pickle.load(f_1)

result = np.zeros(len(dataset))
parser = argparse.ArgumentParser(description='Alignment arguments')
parse_encoder(parser)
args = parser.parse_args()
args.test = True
args.model_path = file_root + args.model_path
model = build_model(args)
# query = nx.gnp_random_graph(8, 0.25)
# target = nx.gnp_random_graph(16, 0.25)
# mat = gen_alignment_matrix(model, query, target,
#         method_type=args.method_type)
# score = np.mean(mat)
# print('done')
# for i, subgraph in enumerate(subgraphs):
#     for j, graph in enumerate(dataset):
#         # if graph.y == 0:
#         #     print(graph.y)
#         print(i, j)
#         query = subgraph
#         target = to_networkx(graph).to_undirected()
#         mat = gen_alignment_matrix(model, query, target,
#                                    method_type=args.method_type)
#         score = np.mean(mat)
#         if score > 0 and graph.y == 0:
#             result[i] += 1
# print(result)
