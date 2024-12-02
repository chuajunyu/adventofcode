from collections import defaultdict

from tools import extract_input

input = extract_input(r"input14.txt")


def get_collinear(point_1, point_2):
    p1x, p1y = point_1
    p2x, p2y = point_2
    if p1x == p2x:
        start = min(p1y, p2y)
        end = max(p1y, p2y)
        return [(p1x, y) for y in range(start, end + 1)]
    elif p1y == p2y:
        start = min(p1x, p2x)
        end = max(p1x, p2x)
        return [(x, p1y) for x in range(start, end + 1)]


def form_rock_map(input):
    rock_map = defaultdict(lambda: '.')
    lowest_y = 0
    for line in input:
        line = line.split(' -> ')

        line = [eval(coord) for coord in line]

        for i, coord in enumerate(line[:-1]):
            for coord in get_collinear(coord, line[i + 1]):
                x, y = coord
                if y > lowest_y:
                    lowest_y = y
                rock_map[coord] = '#'

    return rock_map, lowest_y
        

def display_rock_map(rock_map):
    for y in range(0, 5):
        line = ''
        for x in range(498, 503):
            line += rock_map[(x, y)]
        print(line)


def count_sand(input, has_floor):
    rock_map, lowest_y = form_rock_map(input)
    sand_count = 0
    current_sand = None
    while True:
        # display_rock_map(rock_map)
        if not current_sand:
            current_sand = 500, 0

        curr_x, curr_y = current_sand

        if has_floor:
            if curr_y == lowest_y + 1:
                rock_map[(curr_x, curr_y)] = 'O'
                sand_count += 1
                current_sand = None
                continue
        else:
            if curr_y > lowest_y:
                return sand_count

        # drop down
        if rock_map[(curr_x, curr_y + 1)] == '.':
            current_sand = curr_x, curr_y + 1
            continue
        # drop left
        elif rock_map[(curr_x - 1, curr_y + 1)] == '.':
            current_sand = curr_x - 1, curr_y + 1
            continue
        # drop right
        elif rock_map[(curr_x + 1, curr_y + 1)] == '.':
            current_sand = curr_x + 1, curr_y + 1
            continue
        # cannot move
        else:
            if (curr_x, curr_y) == (500, 0):
                return sand_count
            rock_map[(curr_x, curr_y)] = 'O'
            sand_count += 1
            current_sand = None


# print("Part 1: ", count_sand(input, False))
print("Part 2: ", count_sand(input, True))
