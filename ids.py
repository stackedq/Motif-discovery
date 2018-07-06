from common import *

created_motifs_by_far = []
global_counter = 0


def calculate_hamming_distance(string, motif, goal, length):
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


def is_motif_valid(motif, goal, length):
    valid = True
    for string in input_strings:
        if calculate_hamming_distance(string, motif, goal, length) == False:
            valid = False
    return valid


def IDS(state, goal, limit=100):
    global global_counter
    if is_motif_valid(state, goal, limit):
        print_success(state + ' is a valid motif.')
        global_counter += 1
        # return state
    neighbor_motifs = [a for a in create_neighbor_motifs(
        state, limit) if str(a) == a]

    for neighbor_motif in neighbor_motifs:
        print('Checking ' + neighbor_motif + '...', end="\r")
        IDS(neighbor_motif, goal, limit)


def discover_motifs(length, desired_hamming_distance):
    starter_motif = create_neighbor_motifs(None, length)
    IDS(starter_motif, desired_hamming_distance, length)


def create_neighbor_motifs(motif, length):
    if motif is None:
        motif = ''
        for i in range(0, length):
            motif += motif_characters[0]
        created_motifs_by_far.append(motif)
        return motif
    indexes = find_all(motif, motif_characters[0])
    # print(indexes)
    if len(indexes) == 0:
        return [-1]
    neighbor_motifs = []
    for index in indexes:
        for char in motif_characters:
            s = list(motif)
            s[index] = char
            new_motif = "".join(s)
            if handled_previously(new_motif) != True:
                created_motifs_by_far.append(new_motif)
                neighbor_motifs.append(new_motif)
    return neighbor_motifs


def handled_previously(motif):
    return motif in created_motifs_by_far


def get_nth_substrings(length, string):
    substrings = []
    for limit in range(0, len(input_strings[0]) - length):
        substrings.append(string[limit:limit + length])
    return substrings


st = start_time()
discover_motifs(input_motif_length, input_hamming_distance)
if global_counter > 0:
    print_success(str(global_counter) + ' motif with the length of ' +
                  str(input_motif_length) + ' found.')
else:
    print_error('No motifs with length of ' +
                str(input_motif_length) + ' were found.')
end_time(st)
