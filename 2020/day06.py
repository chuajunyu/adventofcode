"""
Advent of Code 2020

Day 6
"""

FILENAME = "input.txt"

with open(FILENAME) as file:
    input = file.read()
    input = input.split('\n\n')

# Don't remove the newline just in case part 2 needs to differentiate between individuals
   

# Part 1

def count_any_yes(input):
    input = [line.replace('\n', '') for line in input]
    return [len(set(line)) for line in input]

print('Part 1: {}'.format(sum(count_any_yes(input))))


# Part 2

def count_all_yes(input):
    input = [line.split('\n') for line in input]
    all = []
    for group in input:
        group = [set(person) for person in group]
        all_yes = group[0].intersection(*group[1:])
        all.append(len(all_yes))
    return all

print('Part 2: {}'.format(sum(count_all_yes(input))))


# Answers: 6680, 3117
