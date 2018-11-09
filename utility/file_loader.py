###################################
#####LAST MODIFIED BY MATTHIEU#####
###################################

from utility.constants import *
from os import listdir
from os.path import isfile, join


def file_loader():
    """""
    Returns 3 lists :
        list_sequence_files is the list of sequence_filenames
        list_process_files is the list of processes_filenames
        file_labels is a list of bools where file_labels[i] == 1 if the ith file is a malware
    """""
    list_sequence_files = [f for f in listdir(TRAINING_DIR) if
                           (isfile(join(TRAINING_DIR, f)) and f[-23:] == 'behavior_sequence.txt')]
    list_process_files = [f for f in listdir(TRAINING_DIR) if
                          (isfile(join(TRAINING_DIR, f)) and f[-14:] == 'generation.txt')]
    file_labels = parse_label(f"{MAIN_DIR}/{LABEL_FILE_NAME}")
    return list_sequence_files, list_process_files, file_labels

def parse_label(label_file) :
    with open(label_file) as infile:
        labels = []
        for line in infile :
            labels += [line]
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
            sequences_triplets += [line]
        return sequences_triplets
