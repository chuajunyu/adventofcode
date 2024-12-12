def extract_input(filename):
    """
    Reads a text file into a list of strings, where each string corresponds
    to a line in the text file.

    Removes the trailing newline at the end of each string.
    """
    with open(filename) as file:
        input = file.readlines()

    input = [line.strip("\n") for line in input]

    return input

def parse_map(input):
    topo_map = {}
    trailheads = []
    for x, row in enumerate(input):
        for y, char in enumerate(row):
            topo_map[(x, y)] = int(char)
            if char == "0":
                trailheads.append((x, y))
    return topo_map, trailheads


def dfs(topo_map, start, visited):
    found = set()
    curr_elevation = topo_map[start]

    if curr_elevation == 9:
        found.add(start)
        return found

    # Find all neighbours that are traversable that are not in the visited list
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_x = start[0] + dx
        new_y = start[1] + dy
        new_pos = (new_x, new_y)

        if new_pos in visited or new_pos not in topo_map:
            continue

        new_elevation = topo_map[new_pos]

        if new_elevation == curr_elevation + 1:
            visited.add(new_pos)    
            found = found.union(dfs(topo_map, new_pos, visited))

    return found

def part1(input):
    topo_map, trailheads = parse_map(input)

    count = 0
    for th in trailheads:
        visited = set()
        visited.add(th)
        found = dfs(topo_map, th, visited)
        count += len(found)
    return count

def dfs2(topo_map, start, visited):
    found = 0
    curr_elevation = topo_map[start]

    if curr_elevation == 9:
        found += 1
        return found

    # Find all neighbours that are traversable that are not in the visited list
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_x = start[0] + dx
        new_y = start[1] + dy
        new_pos = (new_x, new_y)

        if new_pos in visited or new_pos not in topo_map:
            continue

        new_elevation = topo_map[new_pos]

        if new_elevation == curr_elevation + 1: 
            found += dfs2(topo_map, new_pos, visited)

    return found


def part2(input):
    topo_map, trailheads = parse_map(input)

    count = 0
    for th in trailheads:
        visited = set()
        visited.add(th)
        found = dfs2(topo_map, th, visited)
        count += found
    return count


if __name__ == "__main__":
    input = extract_input("input.txt")
    test_input = extract_input("test.txt")

    # print(part1(test_input))  # Should be 36
    # print(part2(test_input))  # Should be 2858

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
