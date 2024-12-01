from tools import extract_input


input = extract_input(r"input08.txt")

def make_visibility_map(input):
    depth = len(input)
    width = len(input[0])
    vis_map = [[1] + [0] * (width - 2) + [1] for _ in range(depth)]
    for i in [0, depth - 1]:
        vis_map[i] = [1] * width
    return vis_map


def check_visibility(input, vis_map):
    # Check rows
    for row_id, row in enumerate(input):
        tallest = -1
        for col_id, tree in enumerate(row):
            if int(tree) > tallest:
                vis_map[row_id][col_id] = 1
                tallest = int(tree)

        tallest = -1
        length = len(row) - 1
        for col_id, tree in enumerate(reversed(row)):
            if int(tree) > tallest:
                vis_map[row_id][length - col_id] = 1
                tallest = int(tree)
    
    # Check columns
    depth = len(input[0])
    for col_id in range(depth):
        col = [row[col_id] for row in input]

        tallest = -1
        for row_id, tree in enumerate(col):
            if int(tree) > tallest:
                vis_map[row_id][col_id] = 1
                tallest = int(tree)

        tallest = -1
        length = depth - 1
        for row_id, tree in enumerate(reversed(col)):
            if int(tree) > tallest:
                vis_map[length - row_id][col_id] = 1
                tallest = int(tree)

    visible_trees = sum([sum(row) for row in vis_map])
    return visible_trees


def calculate_scenic_score(input, coordinates):
    tree_x, tree_y = coordinates
    height = int(input[tree_y][tree_x])

    left = 0
    for tree in input[tree_y][tree_x - 1:: -1]:
        if int(tree) >= height:
            left += 1
            break
        else:
            left += 1

    right = 0
    for tree in input[tree_y][tree_x + 1:]:
        if int(tree) >= height:
            right += 1
            break
        else:
            right += 1

    col = [row[tree_x] for row in input]

    up = 0
    for tree in col[tree_y - 1:: -1]:
        if int(tree) >= height:
            up += 1
            break
        else:
            up += 1

    down = 0
    for tree in col[tree_y + 1:]:
        if int(tree) >= height:
            down += 1
            break
        else:
            down += 1

    return left * right * up * down


def find_highest_scenic_score(input):
    highest = 0
    for row_id, row in enumerate(input):
        for col_id, _ in enumerate(row):
            score = calculate_scenic_score(input, (col_id, row_id))
            if score > highest:
                highest = score
    return highest


vis_map = make_visibility_map(input)
print("Part 1: ", check_visibility(input, vis_map))
print("Part 2: ", find_highest_scenic_score(input))
