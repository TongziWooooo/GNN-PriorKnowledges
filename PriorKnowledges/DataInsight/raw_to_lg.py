from convert_data_format import read_file
import os

dataset_name = "IMDBBINARY"
graphs, graph_labels = read_file("./data/{}/{}", dataset_name)
root_result = "./data/{}/result/".format(dataset_name)

if not os.path.exists(root_result):
    os.makedirs(root_result)
with open("./data/{}/result/{}_input.lg".format(dataset_name, dataset_name), "w") as f_write:
    for i, graph in enumerate(graphs):
        label = graph_labels[i]
        f_write.write("t # " + str(i) + "_" + str(label) + "\n")

        first_node_id = int(graph[0]["id"])
        edges = []
        for j, node in enumerate(graph):
            if "label" not in node:
                node["label"] = "0"
            f_write.write("v " + str(node["id"] - first_node_id) + " " + node["label"] + "\n")
            for neighbor in node["neighbor"]:
                neighbor = int(neighbor)
                if neighbor > node["id"]:
                    edges.append((str(node["id"] - first_node_id), str(neighbor - first_node_id)))

        for edge in edges:
            f_write.write("e " + edge[0] + " " + edge[1] + " 0" + "\n")
