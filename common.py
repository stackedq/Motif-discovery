import time
import re
import random

input_strings = [
    'ggctaggctgaagcgatgattcgccggactggaacactgcatccgtccatataaccgctcttcgtccccatatcccgtcaatagaaactgacagccttaa',
    'accatccgctagagcatgcctgttgggaaccaccctcgttgatcccgccttataaggtctgcaccgagacggtcactcccctcgatgtatggagtaaaac',
    'gagcaggcgatggcggcctagctgctgaatctctctatatacatgcaatcaatgcgtcgtctgtgcgcccggaggagattagacaacatcaatacgaaac',
    'gggcagggacgtaccatggtaagacgagaatataggccgcatgctacacaaccccaatacgtaggttatatggcggcatggcgtaatattccgtgtactg'
]

input_motif_length = 7
input_hamming_distance = 1
motif_characters = ['a', 'c', 'g', 't']
all_created_motifs=[]

class tcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'


def print_success(string):
    print(tcolors.OKGREEN + string + tcolors.ENDC)

def print_error(string):
    print(tcolors.FAIL + string + tcolors.ENDC)

def print_warning(string):
    print(tcolors.WARNING + string + tcolors.ENDC)

def start_time():
    return time.clock()

def end_time(start_time):
    print('  -- Done in: ' + str(time.clock() - start_time) + ' seconds.')

def find_all(string, sub):
    return [m.start() for m in re.finditer(sub, string)]

def calculate_hamming_distance(substring, motif):
    error = 0
    for i in range(0, len(motif)):
        if substring[i] != motif[i]:
            error += 1
    return error


def generate_random_potential_motif():
    potential_motif = ''
    for i in range(0, input_motif_length):
        potential_motif += random.choice(motif_characters)
    return potential_motif

def get_nth_substrings(length, string):
    substrings = []
    for limit in range(0, len(input_strings[0]) - length):
        substrings.append(string[limit:limit + length])
    return substrings



def validate_by_hamming_distance(string, motif, goal, length):
    string_motifs = get_nth_substrings(length, string)
    valid = False
    for smotif in string_motifs:
        if valid != True:
            error = 0
            for i in range(0, length):
                if smotif[i] != motif[i]:
                    error += 1
            if error <= goal:
                valid = True
                break
    return valid


def is_motif_valid(motif, goal=input_hamming_distance, length=input_motif_length):
    valid = True
    for string in input_strings:
        if validate_by_hamming_distance(string, motif, goal, length) == False:
            valid = False
    return valid


def generate_adjecent_motif(motif):
    this_motif_characters = list(motif)
    random_index = random.randint(0, len(motif) - 1)
    random_char = random.choice(motif_characters)
    while motif[random_index] == random_char:
        random_char = random.choice(motif_characters)
    this_motif_characters[random_index] = random_char
    generated_motif = "".join(this_motif_characters)
    if generated_motif in all_created_motifs:
        return generate_adjecent_motif(motif)
    return generated_motif
