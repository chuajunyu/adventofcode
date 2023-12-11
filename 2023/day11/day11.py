from utils import read_input_lines

input = read_input_lines("input.txt")


def expand_universe(input):
    input = [line for line in input]
    i = 0
    while i < len(input):
        if all([(char == '.') for char in input[i]]):
            input.insert(i, "." * len(input[i]))
            i += 2
        else:
            i += 1

    j = 0
    while j < len(input[0]):
        if all([line[j] == '.' for line in input]):
            input = [(line[:j] + '.' + line[j:]) for line in input]
            j += 2
        else:
            j += 1
    return input


def map_galaxy_coordinates(input):
    galaxy_map = {}
    curr = 0
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '#':
                galaxy_map[curr] = (y, x)
                curr += 1
            else:
                continue
    return galaxy_map


def find_shortest_path(coord1, coord2):
    y1, x1 = coord1
    y2, x2 = coord2
    return abs(y1 - y2) + abs(x1 - x2)


def part1(input):
    input = expand_universe(input)
    galaxy_map = map_galaxy_coordinates(input)
    galaxies = list(galaxy_map.keys())

    total = 0
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1:]:
            total += find_shortest_path(galaxy_map[galaxy], galaxy_map[other_galaxy])
    
    return total


print(part1(input))


def expand_universe_sparse(input, scale):
    galaxy_map = map_galaxy_coordinates(input)
    
    # Find all the rows and columns to be expanded
    rows = []
    for i, line in enumerate(input):
        if all([(char == '.') for char in line]):
            rows.append(i)

    cols = []
    for j in range(len(input[0])):
        if all([line[j] == '.' for line in input]):
            cols.append(j)

    for galaxy in galaxy_map:
        y, x = galaxy_map[galaxy]
        
        to_add_y = 0
        for row in rows:
            if row < y:
                to_add_y += scale - 1
        
        to_add_x = 0
        for col in cols:
            if col < x:
                to_add_x += scale - 1
        galaxy_map[galaxy] = (y + to_add_y, x + to_add_x)

    return galaxy_map


def part2(input):
    galaxy_map = expand_universe_sparse(input, 1000000)
    galaxies = list(galaxy_map.keys())
    total = 0
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1:]:
            total += find_shortest_path(galaxy_map[galaxy], galaxy_map[other_galaxy])
    
    return total


print(part2(input))

