from operator import mul, add

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


def test_equation(test, numbers, op=[mul, add]):
    if len(numbers) == 1:
        return test == numbers[0]
    
    a, b = numbers[0:2]
    for operation in op:
        if test_equation(test, [operation(a, b)] + numbers[2:], op):
            return True
    return False


def part1(input):
    total = 0
    for line in input:
        test, numbers = line.split(": ")
        test = int(test)
        numbers = list(map(int, numbers.split(" ")))
        if test_equation(test, numbers):
            total += test
    return total


def concat(a, b):
    return int(str(a) + str(b))


def part2(input):
    total = 0
    for line in input:
        test, numbers = line.split(": ")
        test = int(test)
        numbers = list(map(int, numbers.split(" ")))
        if test_equation(test, numbers, [mul, add, concat]):
            total += test
    return total

if __name__ == "__main__":
    input = extract_input("input.txt")
    print(part1(input))
    print(part2(input))

    print(concat(12, 345))