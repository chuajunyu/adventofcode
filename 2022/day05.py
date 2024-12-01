from collections import defaultdict
import copy

from tools import read_all

input = read_all("input05.txt")

position, moves = input.split('\n\n')


def convert_position(position):
    position = position.split('\n')
    length = len(position[0])
    columns = (length + 1) // 4
    output = defaultdict(list)
    for line in position[:-1]:
        for col, i in enumerate(range(1, length - 1, 4), start=1):
            letter = line[i]
            if letter != " ":
                output[col].insert(0, letter)
    return columns, output


number_of_columns, position = convert_position(position)
position_copy = copy.deepcopy(position)


def run_instructions(moves, position, part):
    for instruction in moves.strip('\n').split('\n'):
        instruction = instruction.split(' ')
        number_to_move = int(instruction[1])
        start = int(instruction[3])
        end = int(instruction[5])

        if part == 1:
            for _ in range(number_to_move):
                to_move = position[start].pop()
                position[end].append(to_move)
        else:
            to_move = position[start][-number_to_move:]
            position[start] = position[start][:-number_to_move]
            position[end].extend(to_move)

    final = ''
    for i in range(1, number_of_columns + 1):
        final += position[i][-1]

    return final


print("Part 1: ", run_instructions(moves, position, 1))
print("Part 2: ", run_instructions(moves, position_copy, 2))
