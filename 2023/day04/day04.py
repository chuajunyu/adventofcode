from utils import read_input_lines

input = read_input_lines("input.txt")


def read_card(card):
    _, content = card.split(":")
    winning_num, your_num = content.split(" | ")
    winning_nums = [int(n.strip()) for n in winning_num.strip().split(" ") if n]
    your_nums = [int(n.strip()) for n in your_num.strip().split(" ") if n]

    matched = []
    for num in winning_nums:
        if num in your_nums:
            matched.append(num)
    
    return matched


def part1(input):
    total = 0
    for card in input:
        matched_nums = read_card(card)
        if matched_nums:
            total += 2 ** (len(matched_nums) - 1)
    return total


print(part1(input))


def part2(input):
    tracker = dict()
    for game_id, card in enumerate(input):
        matched_nums = read_card(card)
        if matched_nums:
            curr_copies = tracker.get(game_id, 1)
            for i in range(game_id + 1, game_id + 1 + len(matched_nums)):
                tracker[i] = tracker.get(i, 1) + curr_copies
    
    total = sum([tracker.get(i, 1) for i in range(len(input))])
    return total


print(part2(input))
        
