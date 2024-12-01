from tools import extract_input


input = extract_input(r"input02.txt")


possible_outcomes_1 = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6,
}


possible_outcomes_2 = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7,
}


def decrypt_strategy_1(input):
    total_score = 0
    for round in input:
        opponent, you = round.split(' ')
        total_score += possible_outcomes_1[(opponent, you)]

    return total_score


def decrypt_strategy_2(input):
    total_score = 0
    for round in input:
        opponent, you = round.split(' ')
        total_score += possible_outcomes_2[(opponent, you)]

    return total_score


print("Part 1: ", decrypt_strategy_1(input))
print("Part 2: ", decrypt_strategy_2(input))
