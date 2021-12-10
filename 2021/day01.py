from tools import extract_input


FILENAME = "input.txt"
input = extract_input(FILENAME)
input = [int(i) for i in input]


def count_increase(input):
    counter = 0 
    for i in range(len(input) - 1):
        if input[i + 1] > input[i]:
            counter += 1
    return counter


print("Part 1: ", count_increase(input))

sliding_window = [sum(input[i: i+3])
                  for i in range(len(input) - 2)]

print("Part 2: ", count_increase(sliding_window))
