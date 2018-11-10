import numpy as np

def tree_node_number(tree):
    """
    :param  tree: tree
    :return: the numbre of nodes of the tree
    """
    if not(is_arborescence(tree)):
        raise ValueError('this should be an arborescence')
        #erreur
    return tree.number_of_nodes()


def tree_leaf_number(tree):
    """
    :param  tree: tree
    :return: the numbre of nodes of the tree
    """
    if not(is_arborescence(tree)):
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


def generate_api_calls_proximity_matrix(graph):
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
        romain_matrix[predecessor_api,current_api]+=1

    return romain_matrix
    
    