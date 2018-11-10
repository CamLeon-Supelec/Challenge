from inputs.input_formating import *
from inputs.forest_input_formating import *
from utility.constants import *
from utility.file_loader import *


def final_function(data_i) :
    sequences = parse_sequences(data_i[1])
    processes = parse_processes(data_i[0])
    tree, source = generate_subprocess_tre(processes)
    forest = generate_API_behavior_graph(sequences)
    return forest_input(tree, source, forest)