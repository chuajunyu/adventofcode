from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)
input = input[0].split(',')
input = [int(i) for i in input]


def cost(steps):
    fuel = ((steps + 1) * steps) // 2
    return fuel


def least_fuel(input, cost):
    """
    If there are more crabs with a position greater than the average then it is likely
    for the optimal position to be higher than average and vice versa

    Find least fuel either from positions avg to max or avg to min depending on 
    whether there are more or less crabs greater than avg respectively
    """
    avg = sum(input) // len(input)
    high = max(input)
    low = min(input)
    less_than = more_than = 0

    for crab in input:
        if crab > avg:
            more_than += 1
        elif crab < avg:
            less_than += 1

    diff = more_than - less_than
    direction = diff // abs(diff)  # Direction for range step
    if direction > 0:
        end = high
    else:
        end = low

    least = None
    for position in range(avg, end, direction):
        fuel = 0
        for crab in input:
            fuel += cost(abs(crab - position))
        if least == None or fuel < least:
            least = fuel

    return least


print("Part 1: ", least_fuel(input, lambda x : x))
print("Part 2: ", least_fuel(input, cost))


"""
My solution uses brute force to search for the optimal position
However, it can be deduced that 
Part 1's optimal position is the median (Optimality Property)
Part 2's optimal position is very close to the mean (+/- 1) (Minimise mean squared)
"""
