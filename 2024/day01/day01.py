def extract_input(filename):
    """
    Reads a text file into a list of strings, where each string corresponds
    to a line in the text file.

    Removes the trailing newline at the end of each string.
    """
    with open(filename) as file:
        input = file.readlines()

    # To remove the newline    
    for i in range(len(input)):
        input[i] = input[i].strip('\n')

    return input

def extract_lists(input):
    list1, list2 = [], []
    for row in input:
        left, right = row.split('   ')
        list1.append(int(left))
        list2.append(int(right))
    return list1, list2

def part1(input):
    list1, list2 = extract_lists(input)
    list1.sort()
    list2.sort()
    diff = 0
    for x, y in zip(list1, list2):
        diff += abs(x - y)
    return diff

def part2(input):
    list1, list2 = extract_lists(input)
    score = 0
    for x in list1:
        score += x * list2.count(x)
    return score


if __name__ == '__main__':
    test_input = extract_input('test.txt')
    input = extract_input('input.txt')
    
    # print(f"Test Part 1: {part1(test_input) == 11}")
    # print(f"Test Part 2: {part2(test_input) == 31}")
    
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")