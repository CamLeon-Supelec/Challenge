from inputs.input_formating import *
from inputs.forest_input_formating import *
from utility.constants import *
from utility.file_loader import *


def final_function(num_fichier, data) :
    sequences = parse_sequences(data[1][num_fichier])
    processes = parse_processes(data[0][num_fichier])
    tree, source = generate_subprocess_tre(processes)
    forest = generate_API_behavior_graph(sequences)
    return forest_input(tree, source, forest)