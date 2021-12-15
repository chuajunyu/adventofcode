from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)

cave_map = {(y, x): int(num) 
            for y, line in enumerate(input) 
            for x, num in enumerate(line)}


def neighbours(pos, cave_map):
    y, x = pos
    neighbour = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    valid = [p for p in neighbour if p in cave_map]
    return valid


def find_best_path(cave_map):
    """
    I think this is an implementation of Dijkstra's algorithm

    The goal is to create a visited dictionary that maps
    out the minimal cost of going to any point in the cave.

    The stack keeps track of which points in the cave need
    to have the costs of their adjacent blocks (neighbours) updated.

    When a point in the stack is processed, its neighbours have 
    their costs computed, and then the neighbours are added to the stack,
    so that their neighbours can also have their costs computed.

    Points are added to the stack when:
    1. Their costs are computed for the first time (So now their neighbours cost can also be computed)
    2. Their neighbours cost changes, causing them to update their costs (So now their neighbours cost may change)

    The stack is initialised with only the starting point.
    The algorithm ends when the stack is empty, meaning all points have been updated fully.
    """
    stack = [((0, 0), 0)]
    visited = {(0, 0): 0}

    while stack:

        # Sort to prioritise updating the neighbours of points that are closer to the source. 
        # Updates closer to the source will lead to more updates further down the line.
        # There is no use updating the points near the end, if the points near to the source are 
        # not fully updated, as when they are updated, points near the end will need to be updated again.
        # Reduced time of part 1 from >100s to <1s
        stack.sort(key=lambda x: sum(x[0]), reverse=True)
        pos, cost = stack.pop()
        visited[pos] = cost

        for n in neighbours(pos, cave_map):
            if n not in visited:
                new_cost = cost + cave_map[n]
                visited[n] = new_cost
                stack.append((n, new_cost))

            else:
                new_cost = cost + cave_map[n]
                if new_cost < visited[n]:
                    visited[n] = new_cost

                    # Remove any old instances of this point from the stack.
                    # Due to the priority queue, some instances are pushed to the back.
                    # They should not be processed if a more updated version of the same point is added to the stack,
                    # Otherwise, the old cost will override the more updated cost
                    [stack.remove(old)
                    for old in stack if old[0] == n]
                    stack.append((n, new_cost))
                    
    end = sorted(visited)[-1]
    return visited[end]


def reset(num):
    if num > 9:
        return (num % 9)
    else:
        return num


new_cave_map = {(y+ymul*len(input), x+xmul*len(input)):
                reset((cave_map[y, x] + (ymul + xmul)))
                for y, x in cave_map
                for xmul in range(5)
                for ymul in range(5)}

print('Part 1: ', find_best_path(cave_map)) 
print('Part 2: ', find_best_path(new_cave_map))  # ~12s
