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


def is_report_safe(report):
    report_diff = []
    for i, level in enumerate(report[:-1]):
        report_diff.append(report[i + 1] - level)

    # check if all positive or all negative
    if all([diff > 0 for diff in report_diff]) or all([diff < 0 for diff in report_diff]):
        # check if all within 1 and 3
        if all([1 <= abs(diff) <= 3 for diff in report_diff]):
            return True
    return False
    

def part1(input):
    safe = 0
    for row in input:
        row = row.split(' ')
        report = [int(level) for level in row]

        if is_report_safe(report):
            safe += 1
                
    return safe


def part2(input):
    safe = 0
    for row in input:
        row = row.split(' ')
        report = [int(level) for level in row]
        if is_report_safe(report):
            safe += 1
        else:
            for i, _ in enumerate(report):
                augmented_report = report[:i] + report[i + 1:]
                if is_report_safe(augmented_report):
                    safe += 1
                    break             
    return safe


if __name__ == '__main__':
    test_input = extract_input('test.txt')
    input = extract_input('input.txt')

    # print(f"Test Part 1: {part1(test_input) == 2}")
    # print(f"Test Part 2: {part2(test_input) == 4}")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
