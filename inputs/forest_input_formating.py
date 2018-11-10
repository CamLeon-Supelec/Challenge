def forest_input(process_tree,behavior_sequence_forest)
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
    max = [-1]*vector_size
    min = [99999]*vector_size
    mean = [-1]*vector_size 

    for graph in behavior_sequence_forest :

        x=graph_node_number(graph)
        k=0
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x

        x=rip_diversity(graph)
        k=1
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x
        
        x=api_diversity(graph)
        k=2
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x

        y=graph_structure_stats(graph)

        x=y[0]
        k=3
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x

        x=y[1]
        k=4
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x

        x=y[2]
        k=5
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x

        x=y[3]
        k=6
        if max[k] < x
            max[k] = x
        if min[k] > x
            min[k] = x
        mean[k]+= x

    mean = mean / len(behavior_sequence_forest)

    output+=max+min+mean #concatenate lists
    

def forest_api_frequency(behavior_sequence_forest)
    
    for graph in behavior_sequence_forest :

    #api_frequency : vector of size 3500
    

def forest_romain_matrix(behavior_sequence_forest)
    
    for graph in behavior_sequence_forest :
    #generate_api_calls_proximity_matrix :  matrix of size 3500x3500
