def read_file(read_root, dataset_name, node_attr=False, node_label=False):
    edges = {}
    graphs = []
    graph_labels = []

    if node_attr:
        f_node_attributes = open(read_root.format(dataset_name, dataset_name + "_node_attributes.txt"), "r")
    if node_label:
        f_node_labels = open(read_root.format(dataset_name, dataset_name + "_node_labels.txt"), "r")

    with open(read_root.format(dataset_name, dataset_name + "_A.txt"), "r") as f_A, \
            open(read_root.format(dataset_name, dataset_name + "_graph_indicator.txt"), "r") as f_graph_indicator, \
            open(read_root.format(dataset_name, dataset_name + "_graph_labels.txt"), "r") as f_graph_labels:

        s_a = f_A.readline()  # reading edges
        while s_a:
            e = s_a.strip().replace(",", " ").split()
            a, b = [str(i) for i in e]
            if b in edges:
                edges[b].append(a)
            else:
                edges[b] = [a]
            s_a = f_A.readline()

        s_gl = f_graph_labels.readline()  # reading graphs' label
        while s_gl:
            graph_labels.append(str(int(s_gl.strip()) - 1))
            s_gl = f_graph_labels.readline()

        s_g = f_graph_indicator.readline()  # reading nodes' info
        if node_attr:
            s_na = f_node_attributes.readline()
        if node_label:
            s_nl = f_node_labels.readline()
        n_count = 1
        while s_g:
            g = int(s_g.strip())
            if len(graphs) != g:
                graphs.append([])
            if str(n_count) in edges:
                graphs[-1].append({"id": n_count, "neighbor": edges[str(n_count)]})
            else:
                graphs[-1].append({"id": n_count, "neighbor": []})

            if node_attr:
                na = s_na.strip().replace(",", " ").split()
                graphs[-1][-1]["attr"] = na
                s_na = f_node_attributes.readline()
            if node_label:
                nl = str(s_nl.strip())
                graphs[-1][-1]["label"] = nl
                s_nl = f_node_labels.readline()
            s_g = f_graph_indicator.readline()
            n_count += 1
        return graphs, graph_labels


def write_file(write_root, dataset_name, graphs, graph_labels, global_info=False):
    if global_info:
        f_write_global_info = open(write_root.format(dataset_name, dataset_name) + "_global_info.txt", "w")
    with open(write_root.format(dataset_name, dataset_name) + ".txt", "w") as f_write_dataset:
        f_write_dataset.write(str(len(graph_labels)) + "\n")
        g_count = 0
        print(len(graphs))
        print(len(graph_labels))
        for graph in graphs:
            f_write_dataset.write(str(len(graph)) + " " + graph_labels[g_count] + "\n")
            g_count += 1
            first_node_id = int(graph[0]["id"])
            if global_info:
                graph_attr = graph[0]["attr"][-8:]
                f_write_global_info.write(" ".join(graph_attr) + "\n")
            for node in graph:
                neighbors = [str(int(i) - first_node_id) for i in node["neighbor"]]
                if global_info:
                    f_write_dataset.write(node["label"] + " " + str(len(neighbors)) + " " +
                                          " ".join(neighbors) + " " + " ".join(node["attr"][:-8]) + "\n")
                else:
                    f_write_dataset.write(node["label"] + " " + str(len(neighbors)) + " " +
                                          " ".join(neighbors) + " " + " ".join(node["attr"]) + "\n")


if __name__ == '__main__':
    dataset_name = "ENZYMES"

    graphs, graph_labels = read_file("./data/{}/{}", dataset_name, node_attr=True, node_label=True)
    write_file("../../StructPool/data/{}/{}", dataset_name, graphs, graph_labels)
