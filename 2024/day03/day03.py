def extract_input(filename):
    """
    Reads a text file and returns the content as a string.
    """
    with open(filename) as file:
        input = file.read()

    return input


import re


def part1(input):
    ans = re.findall(r"mul\(\d+,\d+\)", input)
    total = 0
    for match in ans:
        a, b = match[4:-1].split(',')
        prod = int(a) * int(b)
        total += prod
    return total


def part2(input):
    ans = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
    total = 0
    enabled = True
    for match in ans:

        if match == "do()":
            enabled = True
            continue
        if match == "don't()":
            enabled = False
            continue
        
        if enabled:
            a, b = match[4:-1].split(',')
            prod = int(a) * int(b)
            total += prod
    return total


if __name__ == "__main__":
    test_input = extract_input("test.txt")
    input = extract_input("input.txt")

    # print(f"Test Part 1: {part1(test_input) == 161}")
    # print(f"Test Part 2: {part2(test_input) == 48}")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")