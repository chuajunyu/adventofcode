from utils import read_input_lines

input = read_input_lines("input.txt")


def convert_to_sequence(line):
    return [int(i) for i in line.strip().split(" ")]


def find_differences(sequence):
    result = []
    for i, x in enumerate(sequence[1:], 1):
        diff = x - sequence[i - 1]
        result.append(diff)
    return result


def predict_next_element(sequence):
    diff = find_differences(sequence)
    if not any(diff):  # If all are 0s
        return sequence[-1]
    else:
        return sequence[-1] + predict_next_element(diff)


def part1(input):
    total = 0
    for line in input:
        sequence = convert_to_sequence(line)
        total += predict_next_element(sequence)
    return total


print(part1(input))


def predict_prev_element(sequence):
    diff = find_differences(sequence)
    if not any(diff):
        return sequence[0]
    else:
        return sequence[0] - predict_prev_element(diff)


def part2(input):
    total = 0
    for line in input:
        sequence = convert_to_sequence(line)
        total += predict_prev_element(sequence)
    return total


print(part2(input))

