from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)
input = input[0].split(',')
input = [int(i) for i in input]


def memo(func):
    cache = {}
    def memo_func(input):
        if input in cache:
            return cache[input]
        else:
            result = func(input)
            cache[input] = result
            return result
    return memo_func


# Memoization to cache results and improve efficiency
# Reduced time from 8.8s to 0.4s
@memo
def cost(steps):
    fuel = sum([i for i in range(1, steps + 1)])
    return fuel


def least_fuel(input, cost):
    """
    If there are more crabs with a position greater than the average then it is likely
    for the optimal position to be higher than average and vice versa

    Find least fuel either from positions avg to max or avg to min depending on 
    whether there are more or less crabs greater than avg respectively

    Doing this cuts time from 1.2s to 0.4s (with memoization)
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
