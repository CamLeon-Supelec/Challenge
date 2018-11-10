###################################
#####LAST MODIFIED BY MATTHIEU#####
###################################

from utility.constants import *
from os import listdir
from os.path import isfile, join


def file_loader(n_first=0):
    """""
    Returns a list of triples :
        triple[0] = sequence_file_name for the ith software
        triple[1] = process_file_name for the ith software
        triple[2] = label of the ith file 
    """""
    if int == 0:
        list_sequence_files = [f for f in listdir(TRAINING_DIR) if
                               (isfile(join(TRAINING_DIR, f)) and f[-23:] == 'behavior_sequence.txt')]
        list_process_files = [f for f in listdir(TRAINING_DIR) if
                              (isfile(join(TRAINING_DIR, f)) and f[-14:] == 'generation.txt')]
        file_labels = parse_label(f"{MAIN_DIR}/{LABEL_FILE_NAME}")
    else :
        list_sequence_files = [f for f in listdir(TRAINING_DIR)[:n_first] if
                               (isfile(join(TRAINING_DIR, f)) and f[-23:] == 'behavior_sequence.txt')]
        list_process_files = [f for f in listdir(TRAINING_DIR)[:n_first] if
                              (isfile(join(TRAINING_DIR, f)) and f[-14:] == 'generation.txt')]
        file_labels = parse_label(f"{MAIN_DIR}/{LABEL_FILE_NAME}")
    results = [(0, 0, 0)] * len(list_sequence_files)
    for i in range(len(list_sequence_files)):
        results[i] = [(list_sequence_files[i], list_process_files[i], file_labels[i])]
    return results

def parse_label(label_file, n_first):
    with open(label_file) as infile:
        labels = []
        for line in infile:
            labels = list(line)[:n_first]
        return labels


def parse_processes(process_file):
        with open(process_file) as infile:
            processes_couples = []
            for line in infile:
                processes_couples += [(line.split(' -> ')[0], line.split(' -> ')[1])]
            return processes_couples


def parse_sequences(sequence_file):
    with open(sequence_file) as infile:
        sequences_triplets = []
        for line in infile:
            sequences_triplets += line.split(',')
        return sequences_triplets
