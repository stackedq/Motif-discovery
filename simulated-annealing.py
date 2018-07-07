import common
import random
import math

maximum_restarts = 3000
all_created_motifs = []


def calculate_minimum_hamming_distance(motif, string):
    string_motifs = common.get_nth_substrings(
        common.input_motif_length, string)
    error = common.input_motif_length
    for substring in string_motifs:
        substring_error = common.calculate_hamming_distance(substring, motif)
        if substring_error < error:
            error = substring_error
    return error


def calculate_fitness_score(motif):
    fitness_score = 0
    # valid = True
    for string in common.input_strings:
        string_score = calculate_minimum_hamming_distance(motif, string)
        fitness_score += string_score
    return 0 - fitness_score


def start_simulate_annealing():
    motif = common.generate_random_potential_motif()
    all_created_motifs.append(motif)
    probability = 1

    for i in range(0, maximum_restarts):
        if common.is_motif_valid(motif) == True:
            return(motif)
        print('\n')
        temperature = (maximum_restarts - i - 1) / maximum_restarts
        print('temperature:', temperature)
        print('current_motif:', motif)
        if temperature == 0:
            return motif
        next_motif = common.generate_adjecent_motif(motif)
        print('adjecent_motif:', next_motif)
        delta_fitness = calculate_fitness_score(
            next_motif) - calculate_fitness_score(motif)
        print('delta_fitness:', delta_fitness)
        if delta_fitness > 0:
            motif = next_motif
        else:
            probability = math.exp(delta_fitness / temperature)
            random_number = random.randint(0, 100) / 100
            print('probability:', probability)
            if probability > random_number:
                motif = next_motif
                print('Goin down B)')


def map_fitness_to_number(fitness):
    return 100 - (fitness / (len(common.input_strings) + 1) * 100)


st = common.start_time()
answer = start_simulate_annealing()
if common.is_motif_valid(answer) == True:
    common.print_success(answer + ' is a valid motif.')
else:
    common.print_error(answer + ' is not a valid motif.')
common.end_time(st)
