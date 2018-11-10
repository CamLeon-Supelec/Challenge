from inputs.input_formating import *



def forest_input(process_tree, source, behavior_sequence_forest):
    """
    :param  : tree, list of graphs
    :return: vector of size 4+3*7=25
    """
    output=[]
    output+=[tree_node_number(process_tree)]
    output+=[tree_leaf_number(process_tree)]
    output+=[tree_max_children_number(process_tree)]
   # output+=[tree_max_depth(process_tree, source)]

    vector_size = 7
    maxi = np.zeros(vector_size)
    mini = np.array([99999]*vector_size)
    mean = np.zeros(vector_size)

    for graph in behavior_sequence_forest :

        x=graph_node_number(graph)
        k=0
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x

        x=rip_diversity(graph)
        k=1
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x
        
        x=api_diversity(graph)[0]
        k=2
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x

        y=graph_structure_stats(graph)

        x=y[0]
        k=3
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x

        x=y[1]
        k=4
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x

        x=y[2]
        k=5
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x

        x=y[3]
        k=6
        if maxi[k] < x:
            maxi[k] = x
        if mini[k] > x:
            mini[k] = x
        mean[k]+= x

    process_number =len(behavior_sequence_forest)
    if process_number != 0 :
        mean = mean / process_number
    else :
        mean = [0]*vector_size

    output = np.concatenate((output,maxi,mini,mean)) #concatenate lists

    return output
    
def forest_api_frequency(behavior_sequence_forest):
    """
    :param  : list of graphs
    :return: vector of size 3*3561=10500
    """
    
    vector_size = 3561

    max_vector = np.zeros(vector_size)

    for graph in behavior_sequence_forest :
        x = api_frequency(graph)
        for k in range(vector_size):
            if max_vector[k] < x[k]:
                max_vector[k] = x[k]

    return max_vector
    

def forest_romain_matrix(behavior_sequence_forest) : 
    
    maxi = np.zeros((3561, 3561))

    for graph in behavior_sequence_forest :
        romain_matrix= generate_api_calls_proximity_matrix(graph)
        maxi = np.maximum(maxi,romain_matrix) #matrix of size 3500x3500
    return maxi