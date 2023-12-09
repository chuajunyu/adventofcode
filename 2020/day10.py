"""
Advent of Code 2020

Day 10
"""

from tools import extract_input

FILENAME = 'input.txt'

input = [int(x) for x in extract_input(FILENAME)]

# Part 1
def find_dist(input):
    """
    Sort the list, find the difference between each pair
    of adjacent numbers on the list.

    Return the product of the number of differences of 1
    and number of differences of 3
    """
    input.sort()
    # 3 : 1 due to device built in adaptor difference of 3
    difference = {1: 0, 2: 0, 3: 1}

    # Difference with the 0 jolt plane port
    difference[input[0]] += 1

    for i in range(len(input) - 1):
        diff = input[i + 1] - input[i]
        difference[diff] += 1
    return difference[1] * difference[3]


dist = find_dist(input)
print('Part 1: ', dist)


# Part 2
def memo(func):
    """
    Memoization with a cache to speed up recursion
    """
    cache = {}
    def cached_func(input):
        input_key = tuple(input)
        if input_key in cache:
            return cache[input_key]
        else:
            result = func(input)
            cache[input_key] = result
            return result
    return cached_func


@memo
def find_ways(input):
    """
    Essentially a DFS algorithm (Depth First Search)
    (Drawing a tree helps to visualise this)

    1. Sort the input list from smallest to largest
    2. If there is only 1 element in the list, then the
       end is reached, a way has been found, return 1.
    3. Else, take the first element of the list as the start
    4. Loops through the elements in the rest of the list, 
       check if the difference between start and the element
       is less than or equal to 3.
       If so, then that element is one of the possible elements
       to be next in the order of adapters.
    5. Do find_ways on the rest of the list starting
       from that element.
       That way, that element will be treated as the next
       adapter in the order.
       The number of possible ways to reach the end from
       that element with it as the start is returned.
    5. The loop continues until the sum of all the possible ways 
       to reach the end from all the possible next elements is 
       computed.
       This sum is thus the potential ways to reach the end
       with start as the first adapter.
       The sum is returned
    """
    input.sort()
    if len(input) == 1:
        return 1
    first, rest = input[0], input[1:]
    possible_ways = 0
    for i in range(len(rest)):
        if rest[i] - first <= 3:
            possible_ways += find_ways(rest[i:])
        else:
            break
    return possible_ways
    

ways = find_ways([0] + input + [max(input) + 3])
print('Part 2: ', ways)

# Answers: 2664, 148098383347712
