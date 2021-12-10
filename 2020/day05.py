"""
Advent of Code 2020

Day 5
"""

from tools import extract_input

FILENAME = "input.txt"

input = extract_input(FILENAME)

# Part 1

def compute_id(input):
    filled_seats = set()
    for ticket in input:
        row_binary = ticket[:7].replace('F', '0').replace('B', '1')
        col_binary = ticket[7:].replace('L', '0').replace('R', '1')
        
        # Only strip zeros in front if number is not 0000000/000
        if len(row_binary) > 1:
            row_binary.lstrip('0')
        if len(col_binary) > 1:
            col_binary.lstrip('0')

        row = int(row_binary, 2)
        col = int(col_binary, 2)
        id = row * 8 + col

        filled_seats.add(id)

    return min(filled_seats), max(filled_seats), filled_seats

# Part 2

def find_skip():
    low, high, filled = compute_id(input)
    exist = {i for i in range(low, high + 1)}
    skipped_seat = list(exist - filled)
    assert len(skipped_seat) == 1, "There should be only 1 skipped seat"
    return skipped_seat[0]


print("Part 1: {}".format(compute_id(input)[1]))
print("Part 2: {}".format(find_skip()))

# Answer: 864, 739
