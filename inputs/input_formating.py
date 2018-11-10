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
        #erreur
    return tree.number_of_nodes()

def graph_node_number(graph):
    """
    :param  graph: graph
    :return: the numbre of nodes of the graph
    """
    return graph.number_of_nodes()

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
    for node in tree.nodes() :
        number_of_children = node.degree()
        if number_of_children > max_number_of_children:
            max_number_of_children = number_of_children
    return max_number_of_children

def tree_max_depth(tree):
    """
    :param  tree: tree
    :return: the maximum number of children for a node
    """
    max_depth = 1
    #[tree_root_node] = [x for x in tree.nodes() if tree.in_degree(x)==0]
    oriented_tree = nx.bfs_tree(tree)
    last_element = [x for x in oriented_tree.nodes()][-1]

    for predecessor in tree.predecessors_iter(last_element) :
        max_depth+=1

    return(max_depth)

def graph_structure_stats(graph):
    """
    :param  graph: graph
    :return: stats on strongly connected components [number, max_length, mean_length, median_length]
    '
    """
    list_of_length = []
    for list in nx.strongly_connected_component_subgraphs(graph) :
        list_of_length += [len(list)]
    return([len(list_of_length),max(list_of_length), sum(list_of_length)/len(list_of_length), median(list_of_length)])


def generate_api_calls_proximity_matrix(graph):
    # FIXME
    """
    :param  graph: graph
    :return: a matrix for api proximity
    'lines : previous
    'columns : next
    """
    number_of_api = 3561
    
    #matrice  de lien (vaut le nombre de fois où il a été appelé par l'API : pauvre, car ne traduit pas si il est appelé en tant que petit fils) 
    romain_matrix = np.zeros((number_of_api,number_of_api))
    for node in graph.nodes():
        (predecessor_rip,predecessor_api) = graph.predecessors(node)        
        (current_rip,current_api) = node
        current_api = int(current_api[4:])
        predecessor_api = int(predecessor_api[4:])
        romain_matrix[predecessor_api,current_api]+=1

    return romain_matrix

def rip_diversity(graph):
    """
    :param  graph: graph
    :return: a float between 0 and 1. 1 is high diversity. Lower result means lower RIP diversity
    """
    set ={}
    for (rip, api) in graph.nodes :
        set += rip
    return len(set)/nx.number_of_nodes(graph)
    
def api_diversity(graph):
    """
    :param  graph: graph
    :return: tupple of (float in [0,1] for api diversity, number of different APIs)
    """
    set ={}
    for (rip, api) in graph.nodes :
        set += api
    return len(set)/nx.number_of_nodes(graph),len(set)

def rip_frequency(graph):
    """
    :param  graph: graph
    :return: vector of api frequency per api
    """
    number_of_api = 3561
    number_of_process = nx.number_of_nodes(graph)
    api_frequency_list = [0 for i in range(number_of_api)]
    for (rip,api) in graph.nodes:
        api = int(api[4:])
        # INDEX SUR UN FLOAT !
        api_frequency_list[api] += 1
    return(api_frequency_list/number_of_process)


