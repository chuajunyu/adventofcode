from tools import extract_input

input = extract_input(r"input03.txt")


def get_item_priority(item):
    priority = ord(item)
    if priority <= 90:
        priority -= 38
    else:
        priority -= 96
    return priority


def find_errors(input):
    total = 0
    for rucksack in input:
        length = len(rucksack)
        first_comp = set(rucksack[:length//2])
        second_comp = set(rucksack[length//2:])

        for item in first_comp:
            if item in second_comp:
                total += get_item_priority(item)
    return total


def find_badge(input):
    length = len(input)
    total = 0
    for rucksack_start in range(0, length, 3):
        ruck_1, ruck_2, ruck_3 = input[rucksack_start:rucksack_start + 3]
        ruck_1 = set(ruck_1)
        ruck_2 = set(ruck_2)
        ruck_3 = set(ruck_3)
        common_item = ruck_1.intersection(ruck_2, ruck_3)
        for item in common_item:
            total += get_item_priority(item)
    return total


print("Part 1: ", find_errors(input))
print("Part 2: ", find_badge(input))
