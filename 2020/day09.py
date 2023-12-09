"""
Advent of Code 2020

Day 9
"""

from tools import extract_input

FILENAME = 'input.txt'

input = [int(value) for value in extract_input(FILENAME)]


# Part 1
def find_error(input, preamble):
    """
    Returns the value of the number that is not 
    a sum of 2 different numbers in the preamble.
    """
    # Starts looping only after preamble
    for i in range(preamble, len(input)):
        num = input[i]
        preamble_list = input[(i-preamble):i]
        possible = set()

        # Find all possible sums in preamble
        for a in preamble_list:
            for b in preamble_list:
                if a != b:
                    possible.add(a + b)

        if num in possible:
            continue
        else:
            return num


value = find_error(input, 25)
print('Part 1: ', value)


# Part 2
def find_weakness(input, value):
    """
    Finds a contiguous set of at least 2 numbers
    in input which sums up to the value

    Returns the sum of the highest and lowest numbers
    in this contiguous set
    """
    # Loop through all possible set sizes
    for set_size in range(2, len(input)):
        # Loop through all possible start indexes
        for start in range(len(input) - set_size + 1):
            con_set = input[start:start + set_size]
            if sum(con_set) == value:
                return max(con_set) + min(con_set)


weakness = find_weakness(input, value)
print('Part 2: ', weakness)

# Answer: 507622668, 76688505
