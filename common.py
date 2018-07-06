import time
import re

input_strings = [
    'ggctaggctgaagcgatgattcgccggactggaacactgcatccgtccatataaccgctcttcgtccccatatcccgtcaatagaaactgacagccttaa',
    'accatccgctagagcatgcctgttgggaaccaccctcgttgatcccgccttataaggtctgcaccgagacggtcactcccctcgatgtatggagtaaaac',
    'gagcaggcgatggcggcctagctgctgaatctctctatatacatgcaatcaatgcgtcgtctgtgcgcccggaggagattagacaacatcaatacgaaac',
    'gggcagggacgtaccatggtaagacgagaatataggccgcatgctacacaaccccaatacgtaggttatatggcggcatggcgtaatattccgtgtactg'
]

input_motif_length = 7
input_hamming_distance = 1
motif_characters = ['a', 'c', 'g', 't']

OKGREEN = '\033[92m'
ENDC = '\033[0m'
FAIL = '\033[91m'
WARNING = '\033[93m'


def print_success(string):
    print(OKGREEN + string + ENDC)

def print_error(string):
    print(FAIL + string + ENDC)

def print_warning(string):
    print(WARNING + string + ENDC)

def start_time():
    return time.clock()

def end_time(start_time):
    print('- Done in: ' + str(time.clock() - start_time) + ' seconds.')

def find_all(string, sub):
    return [m.start() for m in re.finditer(sub, string)]
