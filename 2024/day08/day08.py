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


def get_antenna_map(input):
    antenna_map = {}
    for x, line in enumerate(input):
        for y, char in enumerate(line):
            if char == ".":
                continue
            
            curr = antenna_map.get(char, [])
            curr.append((x, y))
            antenna_map[char] = curr
    return antenna_map


def find_antinodes(antenna_list, input):
    antinode_set = set()
    for antenna1 in antenna_list:
        for antenna2 in antenna_list:
            if antenna1 == antenna2:
                continue
            x1, y1 = antenna1
            x2, y2 = antenna2
            deltax = x2 - x1
            deltay = y2 - y1
            antinode1 = (x1 - deltax, y1 - deltay)
            antinode2 = (x2 + deltax, y2 + deltay)
            if antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < len(input) and antinode1[1] < len(input[0]):
                antinode_set.add(antinode1)
            if antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < len(input) and antinode2[1] < len(input[0]):
                antinode_set.add(antinode2)
    return antinode_set


def part1(input):
    antenna_map = get_antenna_map(input)
    unique_antinode_set = set()
    for antenna in antenna_map:
        antinode_set = find_antinodes(antenna_map[antenna], input)
        unique_antinode_set = unique_antinode_set.union(antinode_set)
            
    return len(unique_antinode_set)


def find_antinodes2(antenna_list, input):
    antinode_set = set()
    for antenna1 in antenna_list:
        for antenna2 in antenna_list:
            if antenna1 == antenna2:
                continue
            x1, y1 = antenna1
            x2, y2 = antenna2
            deltax = x2 - x1
            deltay = y2 - y1
            antinode1 = antenna1
            antinode2 = antenna2

            while antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < len(input) and antinode1[1] < len(input[0]):
                antinode_set.add(antinode1)
                antinode1 = (antinode1[0] - deltax, antinode1[1] - deltay)
                
            while antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < len(input) and antinode2[1] < len(input[0]):
                antinode_set.add(antinode2)
                antinode2 = (antinode2[0] + deltax, antinode2[1] + deltay)

    return antinode_set


def part2(input):
    antenna_map = get_antenna_map(input)
    unique_antinode_set = set()
    for antenna in antenna_map:
        antinode_set = find_antinodes2(antenna_map[antenna], input)
        unique_antinode_set = unique_antinode_set.union(antinode_set)
            
    return len(unique_antinode_set)


if __name__ == "__main__":
    input = extract_input("input.txt")
    test_input = extract_input("test.txt")

    # print(part1(test_input))  # Should be 14
    # print(part2(test_input))  # Should be 34

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
