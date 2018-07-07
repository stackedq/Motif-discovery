import common
import random

maximum_restarts = 50


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
    valid = True
    for string in common.input_strings:
        string_score = calculate_minimum_hamming_distance(motif, string)
        if string_score > common.input_hamming_distance:
            valid = False
        fitness_score += string_score
    return fitness_score, valid


def check_motif_fitness_score_and_validation(motif):
    motif_is_valid_for_all_strings_inputs = True
    this_motif_fitness_score, is_motif_valid = calculate_fitness_score(motif)
    next_motif = motif
    for i in range(0, maximum_restarts):
        adjecent_motif = common.generate_adjecent_motif(motif)
        adjecent_motif_fitness_score, adjecent_valid = calculate_fitness_score(
            adjecent_motif)
        if adjecent_motif_fitness_score < this_motif_fitness_score:
            print(adjecent_motif + ' is better than ' + next_motif + ' with ' +
                  str(this_motif_fitness_score - adjecent_motif_fitness_score) + ' scores.', end="\r")
            next_motif = adjecent_motif
            break
    if next_motif == motif:
        return motif, this_motif_fitness_score, is_motif_valid
    else:
        return check_motif_fitness_score_and_validation(next_motif)


def start_hill_climbing():
    answers = []
    for i in range(0, maximum_restarts):
        motif, fitness, is_valid = check_motif_fitness_score_and_validation(
            common.generate_random_potential_motif())
        if is_valid == True:
            if not motif in answers:
                answers.append(motif)
                common.print_success(
                    motif + ' is a discovered motif with score of ' + map_fitness_to_number(fitness))
        else:
            common.print_warning(motif + ' is not a motif because of ' +
                                 str(fitness) + ' hamming distance.')
    if len(answers) > 0:
        common.print_success(str(len(answers)) + ' motif(s) with length of ' +
                             str(common.input_motif_length) + ' motifs were discovered.')
    else:
        common.print_error('No motifs with length of ' +
                           str(common.input_motif_length) + ' were found.')


def map_fitness_to_number(fitness):
    return str(int(100 - (fitness / (len(common.input_strings) + 1) * 100)))


st = common.start_time()
start_hill_climbing()
common.end_time(st)
