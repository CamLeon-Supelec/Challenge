from inputs.input_formating import *

def forest_input(process_tree,behavior_sequence_forest):
    """
    :param  : tree, list of graphs
    :return: vector of size 4+3*7=25
    """
    output=[]
    output+=[tree_node_number(process_tree)]
    output+=[tree_leaf_number(process_tree)]
    output+=[tree_max_children_number(process_tree)]
    output+=[tree_max_depth(process_tree)]

    vector_size = 7
    max = np.zeros(vector_size)
    min = np.array([99999]*vector_size)
    mean = np.zeros(vector_size)

    for graph in behavior_sequence_forest :

        x=graph_node_number(graph)
        k=0
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x

        x=rip_diversity(graph)
        k=1
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x
        
        x=api_diversity(graph)
        k=2
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x

        y=graph_structure_stats(graph)

        x=y[0]
        k=3
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x

        x=y[1]
        k=4
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x

        x=y[2]
        k=5
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x

        x=y[3]
        k=6
        if max[k] < x:
            max[k] = x
        if min[k] > x:
            min[k] = x
        mean[k]+= x

    process_number =len(behavior_sequence_forest)
    if process_number != 0 :
        mean = mean / process_number
    else :
        mean = [0]*vector_size

    output = np.concatenate(output,max,min,mean) #concatenate lists
    
def forest_api_frequency(behavior_sequence_forest):
    """
    :param  : list of graphs
    :return: vector of size 3*3561=10500
    """
    
    vector_size = 3561

    max_vector = np.zeros(vector_size)
    min_vector = np.array([99999]*vector_size)
    mean_vector = np.zeros(vector_size)

    for graph in behavior_sequence_forest :
        x = api_frequency(graph)
        for k in vector_size :
            if min_vector[k] < x:
                max[k] = x
            if min[k] > x :
                min[k] = x
            mean[k]+= x
    
    process_number = len(behavior_sequence_forest)
    
    if process_number != 0 :
        for k in vector_size :
            mean[k]= mean[k]/ process_number
    else :
        mean = [0]*vector_size

    return np.concatenate(max_vector, min_vector, mean_vector) 
    

def forest_romain_matrix(behavior_sequence_forest) : 
    
    max = np.zeros((3561,3561))
    min = np.Infinity((3561,3561))
    mean = np.zeros((3561,3561))

    for graph in behavior_sequence_forest :
        romain_matrix= generate_api_calls_proximity_matrix(graph)
        max = np.maximum(max,romain_matrix) #matrix of size 3500x3500
        min = np.minimum(min,romain_matrix)
        mean= np.add(mean,romain_matrix)
    
    process_number = len(behavior_sequence_forest)
    if process_number != 0 :
        mean / process_number
    else : 
        mean = np.zeros((3561,3561))
    return np.concatenate(max, min, mean)