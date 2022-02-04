import json
import numpy as np
import matplotlib.pyplot as plt
dataset_name = "ENZYMES"
dataset_len = 600
graph_path = "data/{}/result/match_result_4_6/motif_stats.output".format(dataset_name)
occ_path = "data/{}/result/match_result_4_6/motif_occ.output".format(dataset_name)
feature_path = "../../StructPool/data/{}/{}_subgraph_info".format(dataset_name, dataset_name)
subgraphs = []
selected_subgraph_list = []
# bias = []

with open(graph_path, 'r') as f_graph:
    for line in f_graph:
        data = json.loads(line)
        subgraphs.append(data)
        flag = False
        for i in range(6):
            for j in range(6):
                if i != j and data['label_{}_net'.format(i)] / data['label_{}_net'.format(j)] > 2:
                    selected_subgraph_list.append(data['index'])
                    flag = True
                    break
            if flag:
                break
        # if data['bias_net'] > 3:
        #     selected_subgraph_list.append(data['index'])
        #     bias.append(data['bias_net'])
# plt.hist(bias, bins=30)
# plt.show()
print(len(selected_subgraph_list))
feature_matrix = np.zeros((dataset_len, len(selected_subgraph_list)))
with open(occ_path, 'r') as f_occ:
    for i, line in enumerate(f_occ):
        data = json.loads(line)
        for graph, count in data['graph_occ_list']:
            if data['index'] in selected_subgraph_list:
                feature_matrix[int(graph)][selected_subgraph_list.index(data['index'])] = count

feature_matrix = np.array(feature_matrix)
np.save(feature_path, feature_matrix)
print('done')
