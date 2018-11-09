#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# Last modified by Muguette#
############################

import networkx as nx

def generate_subprocess_graph(links):
    """
    :param  links: list of childhood tuples (parent -> child)
    :return: the graph of subprocesses 
    """
    G = nx.Graph()
    G.add_edges_from(links)
    print("Generate subprocesses graph of process " + links[0][1] + " -- Number of links : " + len(links))
    return G
