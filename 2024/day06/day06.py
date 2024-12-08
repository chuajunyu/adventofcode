def extract_input(filename):
    """
    Reads a text file into a list of strings, where each string corresponds
    to a line in the text file.

    Removes the trailing newline at the end of each string.
    """
    with open(filename) as file:
        input = file.readlines()

    # To remove the newline    
    for i in range(len(input)):
        input[i] = input[i].strip('\n')

    return input


def parse_map(input):
    map_dict = {}
    for x, line in enumerate(input):
        for y, char in enumerate(line):
            map_dict[(x, y)] = char
            if char == '^':
                start = (x, y)
    return map_dict, start
    

def get_visited(map_dict, curr_position):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    visited = {(curr_position)}
    curr_direction = 0
    while curr_position in map_dict:
        x, y = curr_position
        next_x, next_y = x + directions[curr_direction][0], y + directions[curr_direction][1]

        if (next_x, next_y) not in map_dict:
            break

        if map_dict[(next_x, next_y)] == '#':
            curr_direction = (curr_direction + 1) % 4
            continue

        curr_position = (next_x, next_y)
        visited.add(curr_position)
    return visited


def part1(input):
    map_dict, curr_position = parse_map(input)
    visited = get_visited(map_dict, curr_position)
    return len(visited)


def vis(input, map_dict, visited):
    for x in range(len(input)):
        for y in range(len(input[0])):
            if (x, y) in visited:
                print('X', end='')
            else:
                print(map_dict[(x, y)], end='')
        print()


def test_loop(map_dict, curr_position):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
    curr_direction = 0
    visited = {(curr_position, curr_direction)}

    while curr_position in map_dict:
        x, y = curr_position
        next_x, next_y = x + directions[curr_direction][0], y + directions[curr_direction][1]

        if (next_x, next_y) not in map_dict:
            break

        if map_dict[(next_x, next_y)] == '#':
            curr_direction = (curr_direction + 1) % 4
            continue

        curr_position = (next_x, next_y)
        if (curr_position, curr_direction) in visited:
            return True  # Loop detected
        visited.add((curr_position, curr_direction))
    return False  # No loop detected


def part2(input):
    map_dict, curr_position = parse_map(input)
    visited = get_visited(map_dict, curr_position)
    count = 0
    for spot in visited:
        if spot == curr_position:  # Skip the starting position
            continue
        tmp_dict = map_dict.copy()
        tmp_dict[spot] = '#'
        if test_loop(tmp_dict, curr_position):
            count += 1
    return count
    
if __name__ == "__main__":
    input = extract_input("input.txt")
    print(part1(input))
    print(part2(input))