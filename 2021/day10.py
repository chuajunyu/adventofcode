from typing import Counter
from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)

CHUNK = {'(': ')', '[': ']', '{': '}', '<': '>'}
SYNTAX_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETE_SCORES = {'(': 1, '[': 2, '{': 3, '<': 4}


def find_illegal_char(line):
    to_close = []
    for char in line:
        if char in CHUNK:
            to_close.append(char)
        elif char in CHUNK.values():
            if CHUNK[to_close[-1]] == char:
                to_close.pop()
            else:
                return SYNTAX_SCORES[char]


syntax_error_score = sum([find_illegal_char(line) 
                          for line in input
                          if find_illegal_char(line)])

print("Part 1: ", syntax_error_score)

incomplete = [line for line in input if not bool(find_illegal_char(line))]


def complete_line(line):
    to_close = []
    for char in line:
        if char in CHUNK:
            to_close.append(char)
        elif char in CHUNK.values():
            if CHUNK[to_close[-1]] == char:
                to_close.pop()
    to_close.reverse()
    score = 0
    for char in to_close:
        score *= 5
        score += COMPLETE_SCORES[char]
    return score


autocomplete_scores = [complete_line(line) for line in incomplete]
autocomplete_scores.sort()
print("Part 2: ", autocomplete_scores[len(autocomplete_scores) // 2])
