"""
This short example shows how you can mine frequent graphs using the wrapper
"""
from parsemis.my_parsemis_wrapper import ParsemisMiner
import networkx as nx
import os
dataset = "PROTEINS_full"
miner = ParsemisMiner(
    "../data/{}/result/{}_input_0.lg".format(dataset, dataset),
    "../data/{}/result/{}_output_0.lg".format(dataset, dataset), debug=True,
)
miner.mine_graphs(minimum_frequency="1%")
frequent_graphs = miner.read_output()

# Count our subgraphs
frequent_graph_counts = []
for frequent_graph in frequent_graphs:
    count = 0
    for graph in miner.graphs:
        if graph.graph['id'] in frequent_graph.appears_in:
            count += 1
    frequent_graph_counts.append((count, frequent_graph))

for frequent_graph in sorted(frequent_graph_counts, key=lambda subgraph: subgraph[0], reverse=True):
    if len(frequent_graph[1].graph.edges()) == 0:
        print("%i - %s" % (frequent_graph[0], frequent_graph[1].graph.nodes()))
    else:
        print("%i - %s" % (frequent_graph[0], frequent_graph[1].graph.edges()))
