from common import *
import random

maximum_restarts = 100


def generate_random_potential_motif():
    potential_motif = ''
    for i in range(0, input_motif_length):
        potential_motif += random.choice(motif_characters)
    return potential_motif


def generate_adjecent_motif(motif):
    this_motif_characters = list(motif)
    random_index = random.randint(0, len(motif) - 1)
    random_char = random.choice(motif_characters)
    while motif[random_index] == random_char:
        random_char = random.choice(motif_characters)
    this_motif_characters[random_index] = random_char
    return "".join(this_motif_characters)


def calculate_hamming_distance(substring, motif):
    error = 0
    for i in range(0, len(motif)):
        if substring[i] != motif[i]:
            error += 1
    return error


def calculate_minimum_hamming_distance(motif, string):
    string_motifs = get_nth_substrings(input_motif_length, string)
    error = input_motif_length
    for substring in string_motifs:
        substring_error = calculate_hamming_distance(substring, motif)
        if substring_error < error:
            error = substring_error
    return error


def get_nth_substrings(length, string):
    substrings = []
    for limit in range(0, len(input_strings[0]) - length):
        substrings.append(string[limit:limit + length])
    return substrings


def calculate_fitness_score(motif):
    fitness_score = 0
    valid = True
    for string in input_strings:
        string_score = calculate_minimum_hamming_distance(motif, string)
        if string_score > input_hamming_distance:
            valid = False
        fitness_score += string_score
    return fitness_score, valid


def check_motif_fitness_score_and_validation(motif):
    motif_is_valid_for_all_strings_inputs = True
    this_motif_fitness_score, is_motif_valid = calculate_fitness_score(motif)
    next_motif = motif
    for i in range(0, maximum_restarts):
        adjecent_motif = generate_adjecent_motif(motif)
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
    answers = 0
    for i in range(0, maximum_restarts):
        motif, fitness, is_valid = check_motif_fitness_score_and_validation(
            generate_random_potential_motif())
        if is_valid:
            print(motif + '\n')
        if is_valid == True and (fitness / len(input_strings) < input_hamming_distance):
            answers += 1
            print_success(
                motif + ' is a discovered motif with score of ' + map_fitness_to_number(fitness))
        else:
            print_warning(motif + ' is not a motif because of ' +
                          str(fitness) + ' hamming distance.')
    if answers > 0:
        print_success(str(answers) + ' with length of ' +
                      str(input_motif_length) + ' motifs were discovered.')
    else:
        print_error('No motifs with length of ' +
                    str(input_motif_length) + ' were found.')


def map_fitness_to_number(fitness):
    return str(int(100 - (fitness / len(input_strings) * 100)))


def call_out_answer(motif):
    print_success(motif + ' is an answer.')


start_hill_climbing()
