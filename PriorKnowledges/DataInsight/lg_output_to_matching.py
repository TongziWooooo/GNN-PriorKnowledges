import os
import random
dataset_name = "ENZYMES"
read_path = "data/{}/result/{}_motif_output_100_10.lg".format(dataset_name, dataset_name)
write_dir = "data/{}/result/match_q_4_6/".format(dataset_name)
graphs = []
if not os.path.exists(write_dir):
    os.makedirs(write_dir)
with open(read_path, "r") as f_read:
    for line in f_read:
        if line.startswith('#'):
            freq = line.strip().split(' ')[-1]
            graphs.append({'freq': freq, 'nodes': [], 'edges': []})
        elif line.startswith('t'):
            pass
        elif line.startswith('v'):
            graphs[-1]['nodes'].append({'line': line.strip(), 'degree': 0})
        elif line.startswith('e'):
            a, b = line.strip().split(' ')[1:3]
            e = " ".join(line.strip().split(' ')[:3])
            graphs[-1]['edges'].append(e)
            graphs[-1]['nodes'][int(a)]['degree'] += 1
            graphs[-1]['nodes'][int(b)]['degree'] += 1

# graph_node_count = {}
# for graph in graphs:
#     if str(len(graph['nodes'])) not in graph_node_count:
#         graph_node_count[str(len(graph['nodes']))] = 1
#     else:
#         graph_node_count[str(len(graph['nodes']))] += 1
#
# print(graph_node_count)

for i, graph in enumerate(graphs):
    if not 4 <= len(graph['nodes']) <= 6:
        continue
    with open(write_dir + str(i) + "_" + graph['freq'] + ".graph", "w") as f_write:
        f_write.write("t " + str(len(graph['nodes'])) + " " + str(len(graph['edges'])) + "\n")
        for node in graph['nodes']:
            f_write.write(node['line'] + " " + str(node['degree']) + "\n")
        for edge in graph['edges']:
            f_write.write(edge + "\n")
