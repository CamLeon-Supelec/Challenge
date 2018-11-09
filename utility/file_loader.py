###################################
#####LAST MODIFIED BY MATTHIEU#####
###################################

from utility.constants import *
from os import listdir
from os.path import isfile, join

def file_loader():
    list_sequence_files = [f for f in listdir(VALIDATION_DIR) if
                           (isfile(join(VALIDATION_DIR, f)) and f[-23:] == 'behavior_sequence.txt')]
    list_process_files = [f for f in listdir(VALIDATION_DIR) if
                          (isfile(join(VALIDATION_DIR, f)) and f[-14:] == 'generation.txt')]
    return list_sequence_files, list_process_files


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
