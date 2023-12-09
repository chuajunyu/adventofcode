from utils import read_input_lines

input = read_input_lines("input.txt")
digits = "0123456789"


def extract(input):
    """
    Takes in the input as a list of strings, each
    representing a line
    
    Returns:
    1. Dictionary of (line, start, end) to number
    2. Dictionary of (line, index) to symbol
    """
    num_dict = dict()
    symbol_dict = dict()
    for line_index, line in enumerate(input):
        curr = 0
        start = 0
        digit_temp = ""
        while curr < len(line):
            elem = line[curr]
            if elem in digits:
                if digit_temp == "":
                    start = curr
                digit_temp += line[curr]
            else:
                # add digit if any to the dict
                if digit_temp:
                    num_dict[(line_index, start, curr-1)] = int(digit_temp)
                    digit_temp = ""
                
                if elem != ".":
                    symbol_dict[(line_index, curr)] = elem
            curr += 1
        # Last remaining digit
        if digit_temp:
            num_dict[(line_index, start, curr-1)] = int(digit_temp)
    return num_dict, symbol_dict


# Parsing input to get num_dict and symbol_dict
n, s = extract(input)


def neighbours(coordinates):
    line, start, end = coordinates
    result = [(x, y) for x in [line - 1, line + 1]
                     for y in range(start - 1, end + 2)]
    result += [(line, start - 1), (line, end + 1)]
    return result


def part1(num_dict, symbol_dict):
    total = 0
    for num_coords in num_dict:
        search_area = neighbours(num_coords)
        for coord in search_area:
            if coord in symbol_dict:
                total += num_dict[num_coords]
                break
    return total


print(part1(n, s))


def part2(num_dict, symbol_dict):
    gear_dict = {}
    for num_coords in num_dict:
        search_area = neighbours(num_coords)
        for coord in search_area:
            if symbol_dict.get(coord) == "*":
                if coord not in gear_dict:
                    gear_dict[coord] = []
                gear_dict[coord].append(num_dict[num_coords])
    
    total = 0
    for gear in gear_dict:
        if len(gear_dict[gear]) == 2:
            a, b = gear_dict[gear]
            total += a * b

    return total


print(part2(n, s))

