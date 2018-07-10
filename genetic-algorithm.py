import common
import random
import math
import time

all_created_motifs = []
enough_time = 60


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
    return (common.input_motif_length * len(common.input_strings)) - fitness_score


def mutate(motif):
    new_motif = common.generate_adjecent_motif(motif)
    if handled_previously(new_motif):
        return mutate(motif)
    return new_motif


def reproduce(mom, dad):
    random_index = random.randint(0, common.input_motif_length - 1)
    son = mom[:random_index] + dad[random_index - common.input_motif_length:]
    daughter = dad[:random_index] + \
        mom[random_index - common.input_motif_length:]
    return son, daughter


def handled_previously(motif):
    return motif in all_created_motifs


def generate_initial_population(size):
    population = []
    for i in range(0, size):
        motif = common.generate_random_potential_motif()
        population.append(motif)
        all_created_motifs.append(motif)
    return list(set(population))


def get_random_from_population(population, partner=None):
    random_index = random.randint(0, len(population) - 1)
    motif = population[random_index]
    if partner is not None and partner == motif:
        return get_random_from_population(population, partner)
    else:
        return motif, get_fitness_score_percentage(motif)


def get_fitness_score_percentage(motif):
    return calculate_fitness_score(motif) / (common.input_motif_length * len(common.input_strings))


def implement_genetic_algorithm(size):
    ga_time = common.start_time()
    done = False
    answer = None
    most_close_to_answer = None
    most_close_to_answer_score = 0
    population = generate_initial_population(size)
    while not done:
        new_population = []
        if(len(population) < size):
            for i in range(0, size - len(population)):
                population.append(common.generate_random_potential_motif())
        for i in range(0, len(population)):
            # time.sleep(0.1)
            random_motif_dad, dad_fitness_score = get_random_from_population(
                population)
            best_motif, best_score = random_motif_dad, dad_fitness_score
            random_motif_mom, mom_fitness_score = get_random_from_population(
                population, random_motif_dad)
            if mom_fitness_score > best_score:
                best_motif, best_score = random_motif_mom, mom_fitness_score
            motif_son, motif_daughter = reproduce(
                random_motif_mom, random_motif_dad)
            print(motif_son + ' is child of ' + random_motif_mom +
                  ' and ' + random_motif_dad + '!')
            print(motif_daughter + ' is child of ' + random_motif_mom +
                  ' and ' + random_motif_dad + '!')
            random_probability = random.uniform(0, 1)
            son_score = get_fitness_score_percentage(motif_son)
            if son_score > best_score:
                best_motif, best_score = motif_son, son_score

            elif random_probability < 0.1:
                motif_son = mutate(motif_son)
                son_score = get_fitness_score_percentage(motif_son)
                if son_score > best_score:
                    best_motif, best_score = motif_son, son_score

            daughter_score = get_fitness_score_percentage(motif_daughter)
            if daughter_score > best_score:
                best_motif, best_score = motif_daughter, daughter_score

            elif random_probability < 0.1:
                motif_daughter = mutate(motif_daughter)
                daughter_score = get_fitness_score_percentage(motif_daughter)
                if daughter_score > best_score:
                    best_motif, best_score = motif_daughter, daughter_score

            if son_score > daughter_score:
                new_population.append(motif_son)
            else:
                new_population.append(motif_daughter)

            if most_close_to_answer is None or best_score > most_close_to_answer_score:
                most_close_to_answer, most_close_to_answer_score = best_motif, best_score
            print(best_motif + ' is best motif with fitness of ' +
                  str(get_fitness_score_percentage(best_motif)))
            new_population.append(best_motif)
        population = list(set(new_population))

        if time.clock() - ga_time > enough_time:
            done = True
        for motif in population:
            if common.is_motif_valid(motif) == True:
                done = True
                answer = motif
                break

    if answer is not None:
        return answer
    else:
        return {'best_answer': most_close_to_answer, 'best_score': most_close_to_answer_score}


st = common.start_time()
answer = implement_genetic_algorithm(50)
if str(answer) == answer:
    common.print_success('\n' + answer + ' is a valid motif.')
else:
    common.print_warning('Best found motif is ' +
                         answer['best_answer'] + ' with fitness score of ' + str(answer['best_score']))
common.end_time(st)
