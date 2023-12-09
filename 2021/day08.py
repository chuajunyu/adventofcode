from tools import extract_input

FILENAME = "input.txt"
raw_input = extract_input(FILENAME)

input = []
for line in raw_input:
    patterns, output = line.split('|')
    patterns = patterns.strip().split(' ')
    output = output.strip().split(' ')
    input.append([patterns, output])


def decode(input, output):
    """
    Decodes the output and returns it as a 4 digit integer
    """
    digit_map = {}
    unknowns = []

    # Identify the digits with unique segment numbers
    for pattern in input: 
        length = len(pattern)
        if length == 2:
            digit_map[1] = set(pattern)
        elif length == 4:
            digit_map[4] = set(pattern)
        elif length == 3:
            digit_map[7] = set(pattern)
        elif length == 7:
            digit_map[8] = set(pattern)
        else:
            unknowns.append(set(pattern))

    # Compare segment sets of unknown digits with segment sets of known digits
    # to deduce the rest of the digit segment maps
    for unknown in unknowns:
        if len(unknown) == 6:
            diff_intersect_one =  digit_map[8].difference(unknown).issubset(digit_map[1])
            diff_intersect_four = digit_map[8].difference(unknown).issubset(digit_map[4])

            if diff_intersect_one and diff_intersect_four:
                digit_map[6] = unknown
            elif diff_intersect_four:
                digit_map[0] = unknown
            else:
                digit_map[9] = unknown
            continue

        if len(unknown) == 5:
            if len(unknown.intersection(digit_map[1])) == 2:
                digit_map[3] = unknown
            elif len(unknown.intersection(digit_map[4])) == 3:
                digit_map[5] = unknown
            else:
                digit_map[2] = unknown

    result = ""
    for digit in output:
        for num in digit_map:
            if set(digit) == digit_map[num]:
                result += str(num)

    return int(result)


counter = 0
final_sum = 0
for line in input:
    patterns, output = line
    result = decode(patterns, output)
    final_sum += result
    for i in str(result):
        if i in '1478':
            counter += 1

print('Part 1: ', counter)
print('Part 2: ', final_sum)
