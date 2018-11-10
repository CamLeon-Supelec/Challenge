import numpy as np
from statistics import median
import networkx as nx
from bisect import insort

def tree_node_number(tree):
    """
    :param  tree: tree
    :return: the numbre of nodes of the tree
    """
    if not(nx.is_arborescence(tree)):
        raise ValueError('this should be an arborescence')
    return nx.number_of_nodes(tree)

def graph_node_number(graph):
    """
    :param  graph: graph
    :return: the numbre of nodes of the graph
    """
    return nx.number_of_nodes(graph)

def tree_leaf_number(tree):
    """
    :param  tree: tree
    :return: the numbre of nodes of the tree
    """
    if not(nx.is_arborescence(tree)):
        raise ValueError('this should be an arborescence')
        #erreur
    return(len([x for x in tree.nodes() if tree.out_degree(x)==0 and tree.in_degree(x)==1]))

def tree_max_children_number(tree):
    """
    :param  tree: tree
    :return: the maximum number of children for a node
    """
    max_number_of_children = 1
    for node in tree.nodes():
        number_of_children = nx.degree(tree, node)
        if number_of_children > max_number_of_children:
            max_number_of_children = number_of_children
    return max_number_of_children

def tree_max_depth(tree, source):
    # FIXME
    """
    :param  tree: tree
    :return: the maximum number of children for a node
    """
    max_depth = 1
    #[tree_root_node] = [x for x in tree.nodes() if tree.in_degree(x)==0]
    oriented_tree = nx.bfs_tree(tree)
    last_element = [x for x in oriented_tree.nodes()][-1]

    return(max_depth)

def graph_structure_stats(graph):
    """
    :param  graph: graph
    :return: stats on strongly connected components [number, max_length, mean_length, median_length]
    '
    """
    list_of_length = []
    for list in nx.strongly_connected_components_subgraphs(graph) :
        list_of_length += [len(list)]

    if len(list_of_length) != 0:
        mean = sum(list_of_length)/len(list_of_length)
        med= median(list_of_length)
    else :
        mean=0
        med=0
    return(len(list_of_length),max(list_of_length), mean, med)


def generate_api_calls_proximity_matrix(graph):
    """
    :param  graph: graph
    :return: a matrix for api proximity
    'lines : previous
    'columns : next
    """
    number_of_api = 3561
    
    #matrice  de lien (vaut le nombre de fois où il a été appelé par l'API : pauvre, car ne traduit pas si il est appelé en tant que petit fils) 
    romain_matrix = np.zeros((number_of_api, number_of_api))
    for node in graph.nodes():
        for node_succ in graph.successors(node):
            (successor_rip, successor_api) = node_succ
            (current_rip, current_api) = node
            current_api = int(current_api[4:])
            successor_api = int(successor_api[4:])
            romain_matrix[current_api, successor_api] += 1

    return romain_matrix

def rip_diversity(graph):
    """
    :param  graph: graph
    :return: a float between 0 and 1. 1 is high diversity. Lower result means lower RIP diversity
    """
    number_of_api_calls = nx.number_of_nodes(graph)
    if number_of_api_calls !=0 :
        set_rips =set()
        for (rip,api) in graph.nodes :
            set_rips.add(rip)
        return len(set_rips)/number_of_api_calls
    else:
        return 0
    
def api_diversity(graph):
    """
    :param  graph: graph
    :return: tupple of (float in [0,1] for api diversity, number of different APIs)
    """
    number_of_api_calls = nx.number_of_nodes(graph)
    if number_of_api_calls !=0 :
        set_apis = set()
        for (rip,api) in graph.nodes :
            set_apis.add(api)
        return len(set_apis)/number_of_api_calls,len(set_apis)
    else:
        return 0

    
def api_frequency(graph):
    """
    :param  graph: graph
    :return: vector of api frequency per api
    """
    number_of_api = 3561
    number_of_api_calls = nx.number_of_nodes(graph)
    if number_of_api_calls != 0 :
        api_frequency_list = [0. for i in range(number_of_api)]
        for (rip,api) in graph.nodes :
            api = int(api[4:])
            api_frequency_list[api]+=1
        return(np.array(api_frequency_list)/number_of_api_calls)
    else:
        return 0


