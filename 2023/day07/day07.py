from utils import read_input_lines

input = read_input_lines("input.txt")

"""
The plan
1. create a list of tuples of the hands and their bids
2. write a comparision function that will compare the hands
   and determine which is stronger
3. write a sorting algorithm that applies this comparision
   function to determine the ranking of all the hands
4. iterate through the sorted list and get the total winnings
"""


def create_list_of_hands(input):
    result = []
    for line in input:
        hand, bid = line.split(" ")
        bid = int(bid)
        result.append((hand, bid))
    return result


def type_of_hand(hand):

    SCORING = {
            (5,): 6,
            (1, 4): 5,
            (2, 3): 4,
            (1, 1, 3): 3,
            (1, 2, 2): 2,
            (1, 1, 1, 2): 1,
            (1, 1, 1, 1, 1): 0
    }

    counter = dict()
    for char in hand:
        counter[char] = counter.get(char, 0) + 1

    result = []
    for char in counter:
        result.append(counter[char])

    result.sort()
    
    return SCORING[tuple(result)]



def compare(hand1, hand2):
    CARD_STRENGTH = ['A', 'K', 'Q', 'J', 'T', '9', '8',
                     '7', '6', '5', '4', '3', '2']

    # First compare the type of hand
    hand1_type = type_of_hand(hand1)
    hand2_type = type_of_hand(hand2)

    if hand1_type > hand2_type:
        return 1
    elif hand2_type > hand1_type:
        return -1
    else:
        # Type is the same, compare the char
        for char1, char2 in zip(list(hand1), list(hand2)):
            char1_strength = CARD_STRENGTH.index(char1)
            char2_strength = CARD_STRENGTH.index(char2)

            if char1_strength < char2_strength:
                return 1
            elif char1_strength > char2_strength:
                return -1
            else:
                continue
    return 0


def compare_info(info1, info2):
    return compare(info1[0], info2[0])


import functools

def part1(input):
    hand_list = create_list_of_hands(input)
    sorted_hand_list = sorted(hand_list, key=functools.cmp_to_key(compare_info))
    result = 0
    for rank, (hand, bid) in enumerate(sorted_hand_list, 1):
        result += rank * bid
    return result


print(part1(input))


def type_of_hand2(hand):

    SCORING = {
            (5,): 6,
            (1, 4): 5,
            (2, 3): 4,
            (1, 1, 3): 3,
            (1, 2, 2): 2,
            (1, 1, 1, 2): 1,
            (1, 1, 1, 1, 1): 0
    }

    counter = dict()
    for char in hand:
        counter[char] = counter.get(char, 0) + 1

    result = []
    joker = 0
    for char in counter:
        if char == 'J':
            joker = counter[char]
        else:
            result.append(counter[char])

    if result:
        result.sort()
        result[-1] += joker
    else:
        result = [joker]

    return SCORING[tuple(result)]
    

def compare2(hand1, hand2):
    CARD_STRENGTH = ['A', 'K', 'Q', 'T', '9', '8',
                     '7', '6', '5', '4', '3', '2', 'J']

    # First compare the type of hand
    hand1_type = type_of_hand2(hand1)
    hand2_type = type_of_hand2(hand2)

    if hand1_type > hand2_type:
        return 1
    elif hand2_type > hand1_type:
        return -1
    else:
        # Type is the same, compare the char
        for char1, char2 in zip(list(hand1), list(hand2)):
            char1_strength = CARD_STRENGTH.index(char1)
            char2_strength = CARD_STRENGTH.index(char2)

            if char1_strength < char2_strength:
                return 1
            elif char1_strength > char2_strength:
                return -1
            else:
                continue
    return 0


def compare_info2(info1, info2):
    return compare2(info1[0], info2[0])


def part2(input):
    hand_list = create_list_of_hands(input)
    sorted_hand_list = sorted(hand_list, key=functools.cmp_to_key(compare_info2))
    result = 0
    for rank, (hand, bid) in enumerate(sorted_hand_list, 1):
        result += rank * bid
    return result

print(part2(input))

