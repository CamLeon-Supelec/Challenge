#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# Last modified by Muguette#
############################

import networkx as nx

def generate_subprocess_graph(links):
    """
    :param  links: list of childhood tuples (parent -> child)
    :return: the tree of subprocesses 
    """
    G = nx.DiGraph(Type="Subprocesses")
    G.add_edges_from(links)
    return G

def generate_subprocess_tre(links):
    """
    :param  links: list of childhood tuples (parent -> child)
    :return: the tree of subprocesses
    """
    G = nx.DiGraph(Type="Subprocesses")
    G.add_edges_from(links)
    print("Generate subprocesses graph of process " + links[0][1] + " -- Number of links : " + len(links))
    return G, links[0][0] # return parent with graph


def generate_RIP_behavior_graph(records):
    """
    :param records:list of tuples (process, RIP, API_called)
    :return: the graphs of API_calls of all subprocesses
    """

    # Each subprocess is associated to one graph
    # LIC stands for Last I Checked
    forest_and_LIC = {}  # forest_and_LIC = {subprocess : (graph, LIC)}
    # Equivalent to : 
    #forest = {} # Forest = {subprocess : graph}
    #last_I_checked = {} # last_I_checked = {subprocess : last record (subprocess, _, _)}

    for i, record in enumerate(records):
        subprocess = record[0]
        RIP = record[1]
        API_call = record[2]
        
        if subprocess in forest_and_LIC.keys():
            # This process had been seen before
            process_graph, process_LIC = forest_and_LIC[subprocess]
            # Equivalent to :
            #process_graph = forest[subprocess]
            #process_LIC = last_I_checked[subprocess]
            # This was the RIP of the last record (subprocess, _, _)
            lastRIP = records[process_LIC][1]

            if process_graph.has_edge(lastRIP, RIP):
                # The edge already exist, its weight is incremented
                process_graph[lastRIP][RIP]['weight'] += 1
            else:
                # The edge is created
                process_graph.add_edge(lastRIP, RIP, weight=1)
            
            # We want to add API_call in the list of API_calls associated to this RIP iff it is not in already
            if API_call not in process_graph[RIP]['API_calls']:
                process_graph[RIP]['API_calls'].append(API_call)

        else:
            # This process had not been seen before
            process_graph = nx.DiGraph(process=subprocess)
            
            # We generate the node so that we can add the API_call associated to it
            process_graph.add_node(RIP, API_calls=[API_call])

        # Generate the tuple (graph, LIC) associated to subprocess
        forest_and_LIC[subprocess] = (process_graph, i)

    return [forest_and_LIC[subprocess][0] for subprocess in forest_and_LIC.keys()]

def generate_API_behavior_graph(records):
    """
    :param records:list of tuples (process, RIP, API_called)
    :return: the graphs of API_calls of all subprocesses
    """

    # Each subprocess is associated to one graph
    # LIC stands for Last I Checked
    forest_and_LIC = {}  # forest_and_LIC = {subprocess : (graph, LIC)}
    # Equivalent to : 
    #forest = {} # Forest = {subprocess : graph}
    #last_I_checked = {} # last_I_checked = {subprocess : last record (subprocess, _, _)}

    for i, record in enumerate(records):
        subprocess = record[0]
        RIP = record[1]
        API = record[2]
        
        if subprocess in forest_and_LIC.keys():
            # This process had been seen before
            process_graph, process_LIC = forest_and_LIC[subprocess]
            # Equivalent to :
            #process_graph = forest[subprocess]
            #process_LIC = last_I_checked[subprocess]
            # This was the RIP of the last record (subprocess, _, _)
            lastRIP = records[process_LIC][1]
            lastAPI = records[process_LIC][2]

            if process_graph.has_edge((lastRIP, lastAPI) , (RIP, API)):
                # The edge already exist, its weight is incremented
                process_graph[(lastRIP, lastAPI)][(RIP, API)]['weight'] += 1
            else:
                # The edge is created
                process_graph.add_edge((lastRIP, lastAPI), (RIP, API), weight=1)
            
        else:
            # This process had not been seen before
            process_graph = nx.DiGraph(process=subprocess)

        # Generate the tuple (graph, LIC) associated to subprocess
        forest_and_LIC[subprocess] = (process_graph, i)

    return [forest_and_LIC[subprocess][0] for subprocess in forest_and_LIC.keys()]

