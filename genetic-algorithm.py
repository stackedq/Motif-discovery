import common
import random
import math
import time

all_created_motifs = []
enough_time = 60
fitness_constant = 100


def mutate(motif):
    return common.generate_adjecent_motif(motif)


def reproduce(mom, dad):
    random_index = random.randint(0, common.input_motif_length - 1)
    child = mom[:random_index] + dad[random_index - common.input_motif_length:]
    return child


def generate_initial_population(size):
    population = []
    for i in range(0, size):
        population.append(common.generate_random_potential_motif())
    return population

def get_random_from_population(population):
    random_index = random.randint(0, len(population) - 1)
    return population[random_index]

def implement_genetic_algorithm():
    ga_time = common.start_time()
    done = False
    answer = None
    population = generate_initial_population(100)
    while not done:
        new_population = []
        for i in range(0, len(population)):
            random_motif_dad = get_random_from_population(population)
            random_motif_mom = get_random_from_population(population)
            motif_child = reproduce(random_motif_mom, random_motif_dad)
            print(motif_child + ' is children of ' + random_motif_mom +
                  ' and ' + random_motif_dad + '!', end='\r')
            random_probability = random.randint(0, 100) / 100
            if random_probability < 0.3:
                motif_child = mutate(motif_child)
            new_population.append(motif_child)
        population = new_population

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
        return False


st = common.start_time()
answer = implement_genetic_algorithm()
if answer != False:
    common.print_success('\n' + answer + ' is a valid motif.')
else:
    common.print_error('No motifs were found.')
common.end_time(st)
