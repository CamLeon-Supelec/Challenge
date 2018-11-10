###################################
#####LAST MODIFIED BY MATTHIEU#####
###################################

from utility.constants import *
from os import listdir
from os.path import isfile, join


def file_loader(n):
    """""
    Returns a list of triples :
        triple[0] = sequence_file_name for the ith software
        triple[1] = process_file_name for the ith software
        triple[2] = label of the ith file 
    """""
    list_process_files = []
    list_sequence_files = []
    dirfile = listdir(TRAINING_DIR)
    dirfile.sort()
    for f in dirfile :
        if f[-21:] == 'behavior_sequence.txt' :
            list_sequence_files.append((int(f[-28:-22]), f))
        if f[-14:] == 'generation.txt' :
            list_process_files.append((int(f[-29:-23]), f))
    #list_sequence_files.sort(key=lambda a : a[0])
    #list_process_files.sort(key=lambda a : a[0])
    file_labels = parse_label(f"{MAIN_DIR}/{LABEL_FILE_NAME}")
    results = []
    a = n
    for i in range(len(list_sequence_files)):
        if (a > 1 or a == 0):
            results.append((TRAINING_DIR+'/'+list_sequence_files[i][1], TRAINING_DIR+'/'+list_process_files[i][1], file_labels[i]))
        if a > 1 :
            a -= 1
    return results

def data_loader(start=0, end=2000):
    list_process_files = []
    list_sequence_files = []
    for i in range(start, end):
        si = str(i)
        padding = (6-len(si))*"0"+si
        list_sequence_files.append(f"{TRAINING_DIR}/training_{si}_behavior_sequence.txt")
        list_process_files.append(f"{TRAINING_DIR}/training_{si}_process_generation.txt")

    return list_process_files, list_sequence_files


def labels_loader(start=0, end=2000):
    return parse_label(f"{MAIN_DIR}/{LABEL_FILE_NAMES}")
    

def parse_label(label_file):
    with open(label_file) as infile:
        labels = []
        for line in infile:
            labels = list(line)
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
            sequences_triplets += [line.split()]
        return sequences_triplets
