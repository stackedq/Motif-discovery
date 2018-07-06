import common

created_motifs_by_far = []
global_counter = 0


def IDS(state, goal, limit=100):
    global global_counter
    if common.is_motif_valid(state, goal, limit):
        common.print_success(state + ' is a valid motif.')
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
            motif += common.motif_characters[0]
        created_motifs_by_far.append(motif)
        return motif
    indexes = common.find_all(motif, common.motif_characters[0])
    # print(indexes)
    if len(indexes) == 0:
        return [-1]
    neighbor_motifs = []
    for index in indexes:
        for char in common.motif_characters:
            s = list(motif)
            s[index] = char
            new_motif = "".join(s)
            if handled_previously(new_motif) != True:
                created_motifs_by_far.append(new_motif)
                neighbor_motifs.append(new_motif)
    return neighbor_motifs


def handled_previously(motif):
    return motif in created_motifs_by_far


st = common.start_time()
discover_motifs(common.input_motif_length, common.input_hamming_distance)
if global_counter > 0:
    common.print_success(str(global_counter) + ' motif with the length of ' +
                         str(common.input_motif_length) + ' found.')
else:
    common.print_error('No motifs with length of ' +
                       str(common.input_motif_length) + ' were found.')
common.end_time(st)
