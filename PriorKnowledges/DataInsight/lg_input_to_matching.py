import os
dataset_name = "ENZYMES"
read_path = "data/{}/result/{}_input.lg".format(dataset_name, dataset_name)
write_dir = "data/{}/result/match_d/".format(dataset_name)
graphs = []
if not os.path.exists(write_dir):
    os.makedirs(write_dir)
with open(read_path, "r") as f_read:
    for line in f_read:
        if line.startswith('t # '):
            label = line.strip().replace('t # ', '')
            graphs.append({'label': label, 'nodes': [], 'edges': []})
        elif line.startswith('v'):
            graphs[-1]['nodes'].append({'line': line.strip(), 'degree': 0})
        elif line.startswith('e'):
            a, b = line.strip().split(' ')[1:3]
            e = " ".join(line.strip().split(' ')[:3])
            graphs[-1]['edges'].append(e)
            graphs[-1]['nodes'][int(a)]['degree'] += 1
            graphs[-1]['nodes'][int(b)]['degree'] += 1

for graph in graphs:
    with open(write_dir + graph['label'] + ".graph", "w") as f_write:
        f_write.write("t " + str(len(graph['nodes'])) + " " + str(len(graph['edges'])) + "\n")
        for node in graph['nodes']:
            f_write.write(node['line'] + " " + str(node['degree']) + "\n")
        for edge in graph['edges']:
            f_write.write(edge + "\n")
