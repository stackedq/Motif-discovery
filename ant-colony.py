import common
import random
import math
import time

all_pathes = []
global_counter = 0


def create_colony():
    nodes = []
    for index, string in enumerate(common.input_strings):
        substrings = common.get_nth_substrings(
            common.input_motif_length, string)
        nodes.append({'step': index, 'nodes': substrings})
    return nodes


def create_all_pathes(states, all_path=[], step=0):
    global global_counter
    if len(all_path) == 0:
        for node in states[step]['nodes']:
            all_path.append([node])
        print(all_path)
        create_all_pathes(states, all_path, step + 1)
    else:
        for path in all_path:
            for node in states[step]['nodes']:
                path.append(node)
        print(all_path)
        path_length = len(all_path[0])
        if path_length == 2:
            return
        if path_length == len(common.input_strings) + 1:
            return
        if path_length == len(common.input_strings):
            print('path added')
            global_counter += 1
            all_pathes.append(all_path)

    # return pathes


def implement_ant_colony():
    global global_counter
    states = create_colony()
    # for node in states[0]['nodes']:
    create_all_pathes(states)
    # all_path = []
    # for state in states:
    #     path = []
    #     for node in state['nodes']:
    #         path.append(node)
    #         all_path.append(path)
    # print(all_path)
    # print(str(global_counter) + ' available pathes...')
    # time.sleep(3)
    # print(len(all_pathes))
    # print(all_pathes[0])


st = common.start_time()
best_answer = implement_ant_colony()
# if best_answer != False:
#     common.print_success('\n' + best_answer + ' is a valid motif.')
# else:
#     common.print_error('No motifs were found.')
# common.end_time(st)
