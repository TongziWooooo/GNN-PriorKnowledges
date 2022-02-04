"""
This script is a wrapper script for ParSeMiS

For this example, our graphs are represented using NetworkX

https://www2.informatik.uni-erlangen.de/EN/research/zold/ParSeMiS/index.html
"""
import subprocess
import networkx as nx
import logging as log
import os
import re
import numpy as np


class FrequentGraph:

    def __init__(self, graph, appears_in) -> None:
        super().__init__()
        self._graph = graph
        self._appears_in = appears_in
        self._support = len(self._appears_in)
        self.__rank = None

    def to_string(self):
        if len(self._graph.edges()) == 0:
            return  ",".join(self._graph.nodes())
        else:
            edge_strings = []
            for edge in self._graph.edges():
                labels = ParsemisMiner.get_label_from_edge(self._graph, edge)
                for label in labels:
                    if (nx.is_directed(self._graph)):
                        edge_strings.append("(%s)-[%s]->(%s)" % (edge[0], label, edge[1]))
                    else:
                        edge_strings.append("(%s)-[%s]-(%s)" % (edge[0], label, edge[1]))
            return ", ".join(list(set(edge_strings)))

    @property
    def graph(self):
        return self._graph

    @property
    def support(self):
        return self._support

    @property
    def appears_in(self):
        return self._appears_in

    @property
    def rank(self):
        return self.__rank

    def set_rank(self, rank):
        self.__rank = rank


class ParsemisMiner:
    """
    A basic wrapper for using ParSeMiS.

    The wrapper itself has one required argument, a location to store the input and output files for the graphs
    that are required for parsing.
    """

    def __init__(self, input_path, output_path, debug=True):

        self.parsemis_location = "%s/parsemis.jar" % os.path.dirname(os.path.realpath(__file__))

        if debug:
            self.debug_statement = "-Dverbose=true"
        else:
            self.debug_statement = None

        self.input_file = input_path
        self.output_file = output_path
        self.graphs = self.read_input()

    def mine_graphs(self, **kwargs):
        log.debug("Mining %i graphs" % len(self.graphs))
        self.perform_mining(**kwargs)

    def perform_mining(self, **kwargs):
        commands = ['java', '-jar',
                    "-Xmx10g",
                    self.parsemis_location,
                    "--graphFile=%s" % self.input_file,
                    "--outputFile=%s" % self.output_file,
                    "--minimumFrequency=%s" % kwargs.get('minimum_frequency', '0.05'),
                    "--findPathsOnly=%s" % kwargs.get('find_paths_only', False),
                    "--findTreesOnly=%s" % kwargs.get('find_trees_only', False),
                    "--singleRooted=%s" % kwargs.get('single_rooter', False),
                    "--connectedFragments=%s" % kwargs.get('connectedFragments', True),
                    "--algorithm=%s" % kwargs.get('algorithm', 'gspan'),
                    "--closeGraph=%s" % kwargs.get('close_graph', False),
                    "--subdue=%s" % kwargs.get('subdue', False),
                    "--zaretsky=%s" % kwargs.get('zaretsky', False),
                    "--distribution=%s" % kwargs.get('distribution', 'threads'),
                    "--threads=%s" % kwargs.get('n_threads', 1),
                    "--storeEmbeddings=%s" % kwargs.get('store_embeddings', True)
                    ]
        if self.debug_statement is not None:
            commands.insert(2, self.debug_statement)

        if 'minimum_node_count' in kwargs:
            commands.append("--minimumNodeCount=%i" % kwargs.get('minimum_node_count'))
        if 'maximum_node_count' in kwargs:
            commands.append("--maximumNodeCount=%i" % kwargs.get('maximum_node_count'))
        if 'minimum_edge_count' in kwargs:
            commands.append("--minimumEdgeCount=%i" % kwargs.get('minimum_edge_count'))
        if 'maximum_edge_count' in kwargs:
            commands.append("--maximumEdgeCount=%i" % kwargs.get('maximum_edge_count'))
        if 'maximum_frequency' in kwargs:
            commands.append("--maximumFrequency=%i" % kwargs.get('maximum_frequency'))

        log.debug(commands)
        subprocess.call(commands)

    def read_input(self):
        log.debug("Reading graphs from %s" % self.input_file)
        graphs = []
        graph_id = -1
        with open(self.input_file, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith("t #"):
                    graph_id += 1
                    label = int(line.strip().replace("t # ", "").split("_")[1])
                    graph = nx.Graph(id=graph_id, label=label)
                    graphs.append(graph)
                elif line.startswith("v"):
                    parts = line.split(" ")
                    node_id = parts[1]
                    label = parts[2]
                    graphs[graph_id].add_node(node_id, label=label)
                elif line.startswith("e"):
                    parts = line.split(" ")
                    label = parts[3]
                    graphs[graph_id].add_edge(parts[1], parts[2], label=label)
            return graphs

    def read_output(self):
        """
        Reads an LineGraph file and converts it to a list of NetworkX Graph Objects
        :param file: LineGraph file to read
        :return: A list of LineGraph objects
        """
        log.debug("Reading graphs from %s" % self.output_file)
        frequent_graphs = []

        with open(self.output_file, "r") as f:
            graph_map = {}
            node_map = {}
            graph_id = 0
            for line in f.readlines():
                line = line.strip()
                if line.startswith("t #"):
                    node_map = {}
                    graph_id += 1
                    graph = nx.Graph(id=graph_id, embeddings=[])
                    graph_map[graph_id] = graph
                elif line.startswith("v"):
                    parts = line.split(" ")
                    label = " ".join(parts[2:]).strip('\'')
                    graph_map[graph_id].add_node(label)
                    node_map[parts[1]] = label
                elif line.startswith("e"):
                    parts = line.split(" ")
                    label = " ".join(parts[3:]).strip('\'')
                    graph_map[graph_id].add_edge(node_map[parts[1]], node_map[parts[2]], label=label)
                elif line.startswith("#=>"):
                    graph_map[graph_id].graph['embeddings'].append(line.split(" ")[1])

            for graph in graph_map:
                fg = FrequentGraph(graph_map[graph], graph_map[graph].graph['embeddings'])
                frequent_graphs.append(fg)

        return frequent_graphs

    @staticmethod
    def get_label_from_edge(g, edge, attribute_name='label'):
        edge_attributes = g.get_edge_data(edge[0], edge[1])
        if edge_attributes is None and nx.is_directed(g):
            edge_attributes = g.get_edge_data(edge[1], edge[0])

        labels = []
        if type(g) == nx.MultiDiGraph or type(g) == nx.MultiGraph:
            for index in edge_attributes:
                if attribute_name in edge_attributes[index]:
                    labels.append(edge_attributes[index][attribute_name])
        else:
            if attribute_name in edge_attributes:
                labels.append(edge_attributes[attribute_name])

        return labels

    @staticmethod
    def is_subgraph(graph, subgraph):
        if not set(subgraph.nodes()).issubset(graph.nodes()):
            return False
        else:
            for edge in subgraph.edges():
                return ParsemisMiner.graph_has_edge(graph, subgraph, edge)
        return True

    @staticmethod
    def graph_has_edge(graph, subgraph, edge):
        if graph.has_edge(edge[0], edge[1]) or (not nx.is_directed(graph) and graph.has_edge(edge[1], edge[0])):
            subgraph_edge_labels = ParsemisMiner.get_label_from_edge(subgraph, edge)
            supergraph_edge_labels = ParsemisMiner.get_label_from_edge(graph, edge)
            if ParsemisMiner.shares_edge_label(subgraph_edge_labels, supergraph_edge_labels) \
                    or (len(subgraph_edge_labels) == 0 and len(supergraph_edge_labels) == 0):
                return True
            else:
                return False

    @staticmethod
    def shares_edge_label(list_a, list_b):
        return len(set(list_a).intersection(set(list_b))) > 0

    @staticmethod
    def calculate_dot_product_similarity(sub_graph: nx.Graph, super_graph: nx.Graph):
        a_values = np.ones(len(sub_graph.nodes()) + len(sub_graph.edges()))
        b_values = np.zeros(len(a_values))
        for i, node in enumerate(sub_graph.nodes()):
            if node in super_graph.nodes():
                b_values[i] = 1
        for i, edge in enumerate(sub_graph.edges()):
            if ParsemisMiner.graph_has_edge(super_graph, sub_graph, edge):
                b_values[i + len(sub_graph.nodes())] = 1

        return np.prod(np.column_stack((a_values, b_values)), axis=1).sum() / len(a_values)


    @staticmethod
    def calculate_jaccard_similarity(sub_graph: nx.Graph, super_graph: nx.Graph):
        """
                Calculates the similiarity between a subgraph and a parent
                :param sub_graph:
                :param parent_graph:
                :return:
                """

        set_a = set(sub_graph.nodes()).union(sub_graph.edges())
        set_b = ParsemisMiner._calcuate_set_b(sub_graph, super_graph)

        result = len(set_a.intersection(set_b)) / len(set_a.union(set_b))
        return result

    @staticmethod
    def _calcuate_set_b(sub_graph: nx.Graph, super_graph: nx.Graph):
        set_b = set()
        for node in sub_graph.nodes():
            if node in super_graph.nodes():
                set_b.add(node)
        for edge in sub_graph.edges():
            if ParsemisMiner.graph_has_edge(super_graph, sub_graph, edge):
                set_b.add(edge)
        return set_b