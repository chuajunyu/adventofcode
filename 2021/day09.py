from tools import extract_input
from math import prod

FILENAME = "input.txt"
input = extract_input(FILENAME)
input = [[int(i) for i in line] for line in input]


def find_basin(input, curr_point, found):
    """ DFS search to find all points in a basin """
    x, y = curr_point
    found.add(curr_point)

    to_search = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for point in to_search:
        try:
            x , y = point
            assert x >= 0 and y >= 0, "No indexing from the back"
            value = input[y][x]
            if value != 9 and point not in found:
                found |= find_basin(input, point, found)
        except (IndexError, AssertionError):
            continue                                            
    return found


def solve(input):
    """
    Finds the low points and append them to a list
    Run a DFS search on low points to return a set of points that are in a basin
    Returns sum of low points + 1 and product of top 3 basins
    """
    low_points = []
    basin_sizes = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            low = True
            num = input[y][x]
            to_search = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for point in to_search:
                try:
                    new_x , new_y = point
                    assert new_x >= 0 and new_y >= 0, "No indexing from the back"
                    value = input[new_y][new_x]
                    if not num < value:
                        low = False 
                        break
                except (IndexError, AssertionError):
                    continue
            
            if low:  # Current num is a low point
                low_points.append(num)
                size = len(find_basin(input, (x, y), set()))
                basin_sizes.append(size)
    
    basin_sizes.sort(reverse=True)
    product = prod(basin_sizes[:3])
    return sum([i + 1 for i in low_points]), product


part1, part2 = solve(input)
print("Part 1: ", part1)
print("Part 2: ", part2)

# Alt solution: Use a dictionary mapping coordinates to height
