from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)


def get_position(input):
    x = y = 0
    for line in input:
        direction, magnitude = line.split(" ")
        if direction == "forward":
            x += int(magnitude)
        elif direction == "down":
            y += int(magnitude)
        elif direction == "up":
            y -= int(magnitude)
    return x * y


print("Part 1: ", get_position(input))


def get_new_position(input):
    x = y = aim = 0
    for line in input:
        direction, magnitude = line.split(" ")
        if direction == "forward":
            x += int(magnitude)
            y += aim * int(magnitude)
        elif direction == "down":
            aim += int(magnitude)
        elif direction == "up":
            aim -= int(magnitude)
    return x * y


print("Part 2: ", get_new_position(input))
