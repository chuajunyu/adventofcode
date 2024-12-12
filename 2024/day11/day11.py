def extract_input(filename):
    """
    Reads a text file
    """
    with open(filename) as file:
        input = file.read()

    return input.strip()


import functools


def make_memo(func):
    cache = {}

    def memo_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memo_func

@make_memo
def blink_alt(number, times):
    if times == 0:
        return 1
    
    if number == 0:
        return blink_alt(1, times - 1)
    elif len(str(number)) % 2 == 0:
        length = len(str(number)) // 2
        left = int(str(number)[:length])
        right = int(str(number)[length:])
        return blink_alt(left, times - 1) + blink_alt(right, times - 1)
    else:
        return blink_alt(number * 2024, times - 1)


def blink_x_alt(input_list, x):
    count = 0
    for num in input_list:
        count += blink_alt(num, x)
    return count


def blink(number):
    if number == 0:
        return 1,
    elif len(str(number)) % 2 == 0:
        length = len(str(number)) // 2
        left = int(str(number)[:length])
        right = int(str(number)[length:])
        return left, right
    else:
        return number * 2024,


def row_blink(deduped_row):
    result = {}
    for stone in deduped_row:
        for n in blink(stone):
            result[n] = result.get(n, 0) + deduped_row[stone]
    return result


def blink_x(input_list, x):
    deduped_row = {}
    for num in input_list:
        deduped_row[num] = deduped_row.get(num, 0) + 1
    
    for _ in range(x):
        deduped_row = row_blink(deduped_row)
    
    count = 0
    for stone in deduped_row:
        count += deduped_row[stone]
    
    return count


def part1(input):
    input_list = input.split(" ")
    input_list = [int(x) for x in input_list]
    return blink_x_alt(input_list, 25)


def part2(input):
    input_list = input.split(" ")
    input_list = [int(x) for x in input_list]
    return blink_x_alt(input_list, 75)


if __name__ == "__main__":
    input = extract_input("input.txt")
    test_input = extract_input("test.txt")

    # print(part1(test_input))  # Should be 55312
    # print(part2(test_input))  # ?

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
