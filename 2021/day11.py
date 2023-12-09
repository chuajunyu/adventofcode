from tools import extract_input, convert_map_dict

FILENAME = "input.txt"
input = extract_input(FILENAME)
map_dict = convert_map_dict(input)


def get_neighbours(coordinate):
    """
    Returns a list of valid neigbour coordinates
    """
    x, y = coordinate
    possible_neighbours = [(xn, yn) 
                           for xn in range(x-1, x+2)
                           for yn in range(y-1, y+2)
                           if (xn, yn) != (x, y)]
    return [n for n in possible_neighbours 
            if n in map_dict]


def step():
    """
    Simulates one step
    returns the number of flashes and updated map_dict
    """
    num_flash = 0
    flashed = {}

    for octopus in map_dict:
        map_dict[octopus] += 1
        flashed[octopus] = False

    while True:
        round_flash = 0
        for octopus in map_dict:
            energy = map_dict[octopus]
            if energy > 9:
                neighbours = get_neighbours(octopus)
                for neighbour in neighbours:
                    if not flashed[neighbour]:  # Stop adding if flashed
                        map_dict[neighbour] += 1
                map_dict[octopus] = 0
                flashed[octopus] = True
                round_flash += 1
        if round_flash == 0: # Stop if no more flashes
            break
        num_flash += round_flash
    
    return num_flash


flashes = 0
step_count = 0
while True:
    step_count +=1
    num_flash = step()
    flashes += num_flash
    if step_count == 100:
        print('Part 1: ', flashes)
    if num_flash == 100:
        print('Part 2: ', step_count)
        break
