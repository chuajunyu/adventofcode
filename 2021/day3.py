from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)


def find_common(binarylist):
    threshold = len(binarylist) / 2
    amt = sum([int(bit) for bit in binarylist])
    if amt > threshold:
        return '0', '1'
    elif amt < threshold:
        return '1', '0'
    else:
        return '0', '1'  # Default if equal


def find_power(input):
    length = len(input[0])
    gamma = epsilon = ""

    for pos in range(length):
        binarylist = [num[pos] for num in input]
        least, most = find_common(binarylist)
        gamma += most
        epsilon += least

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return epsilon * gamma


print("Part 1: ", find_power(input))


def find_rating(input, get_least):
    length = len(input[0])
    for pos in range(length):
        binarylist = [num[pos] for num in input]
        least, most = find_common(binarylist)

        if get_least:
            input = [num for num in input 
                     if num[pos] == least]
        else:
            input = [num for num in input
                     if num[pos] == most]

        if len(input) == 1:
            break
    return int(input[0], 2)


co2 = find_rating(input, True)
o2 = find_rating(input, False)
print("Part 2 :", co2 * o2)


# Alternative solution for part 1
def get_power(input):
    """
    An alernative method using nested loops
    This takes less time to compute than the above method 
    0.00199s vs 0.00299s
    """
    length = len(input[0])
    gamma = epsilon = ""

    for pos in range(length):
        counter = {'0': 0, '1': 0}
        for num in input:
            counter[num[pos]] += 1    
        least, most = sorted(counter, key=lambda x: counter[x])
        gamma += most
        epsilon += least

    gamma = int(gamma,2)
    epsilon = int(epsilon, 2)
    return epsilon * gamma


print("Part 1: ", get_power(input))
