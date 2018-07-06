
input_strings = [
    'ggctaggctgaagcgatgattcgccggactggaacactgcatccgtccatataaccgctcttcgtccccatatcccgtcaatagaaactgacagccttaa',
    'accatccgctagagcatgcctgttgggaaccaccctcgttgatcccgccttataaggtctgcaccgagacggtcactcccctcgatgtatggagtaaaac',
    'gagcaggcgatggcggcctagctgctgaatctctctatatacatgcaatcaatgcgtcgtctgtgcgcccggaggagattagacaacatcaatacgaaac',
    'gggcagggacgtaccatggtaagacgagaatataggccgcatgctacacaaccccaatacgtaggttatatggcggcatggcgtaatattccgtgtactg'
]

input_motif_length = 6
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
