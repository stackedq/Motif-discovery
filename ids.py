import common

created_motifs_by_far = []
global_counter = 0
answers = []
destoryers = []


def IDS(state, goal, limit=100, stop=False):
    global global_counter
    all_neighbors = []
    for motif in state:
        all_neighbors.append(create_neighbor_motifs(motif))
    all_neighbors = [item for sublist in all_neighbors for item in sublist]
    for motif in all_neighbors:
        print('Checking ' + motif + '...', end='\r')
        if common.is_motif_valid(motif) == False:
            all_neighbors.remove(motif)
            if motif not in destoryers:
                destoryers.append(motif)
        elif len(motif) == limit:
            answers.append(motif)
            common.print_success(motif + ' is a valid motif.')
            global_counter += 1
    if len(all_neighbors[0]) < limit:
        IDS(all_neighbors, goal, limit, True)
    return


def discover_motifs(length, desired_hamming_distance):
    starter_motifs = create_neighbor_motifs(None)
    IDS(starter_motifs, desired_hamming_distance, length)


def create_neighbor_motifs(motif):
    neighbor_motifs = []
    if motif is None:
        motif = ''
    for i in range(0, len(common.motif_characters)):
        should_pass = True
        neighbor_motif = motif + common.motif_characters[i]
        if any(destroyer in motif for destroyer in destoryers):
            should_pass = False
        if should_pass == True:
            neighbor_motifs.append(neighbor_motif)
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
