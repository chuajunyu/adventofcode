from tools import extract_input

input = extract_input(r"input12.txt")


def convert_map_dict(input, datatype):
    """
    Converts a nested list map into a dictionary
    With key value pairs of tuple coordinates to value
    """
    start = 0
    end = 0
    map_dict = {}
    other_starts = list()
    for y, row in enumerate(input):
        for x, value in enumerate(row):
            map_dict[(x, y)] = datatype(value)
            
            if value == 'S':
                start = (x, y)

            if value == 'E':
                end = (x, y)

            if value == 'a':
                other_starts.append((x, y))
            
    return map_dict, start, end, other_starts


def get_height(letter):
    height_map = "abcdefghijklmnopqrstuvwxyz"
    if letter in height_map:
        height = height_map.index(letter)
    elif letter == 'S':
        height = height_map.index('a')
    elif letter == 'E':
        height = height_map.index('z')
    return height


def get_neighbours(map_dict, coordinates):
    x_coord, y_coord = coordinates
    potential_neighbours = [(x_coord + 1, y_coord),
                            (x_coord - 1, y_coord),
                            (x_coord, y_coord + 1),
                            (x_coord, y_coord - 1)]
    return [neighbour for neighbour in potential_neighbours if neighbour in map_dict]


def dijkstra(map_dict, start, end):
    visited = {start}
    shortest_paths = {start: 0}

    set_all_vertices = set(map_dict)

    while end != set_all_vertices:
        possible = list()
        for v in visited:
            to_search = [n for n in get_neighbours(map_dict, v)]
            v_height = get_height(map_dict[v])

            for w in to_search:
                w_height = get_height(map_dict[w])
                if w_height <= v_height + 1:
                    cost = shortest_paths[v] + 1
                    possible.append((cost, v, w))

        possible.sort()
        cost, v, w = possible[0]
        visited.add(w)
        shortest_paths[w] = cost
    return shortest_paths[end]

      
def bfs(map_dict, start, end):
    visited = {start}
    shortest_paths = {start: 0}

    queue = [start]

    while queue:
        curr_point = queue.pop(0)
        curr_height = get_height(map_dict[curr_point])
        to_search = [n for n in get_neighbours(map_dict, curr_point) if n not in visited]

        for v in to_search:
            v_height = get_height(map_dict[v])
            if v_height <= curr_height + 1:
                visited.add(v)
                shortest_paths[v] = shortest_paths[curr_point] + 1
                queue.append(v)
    return shortest_paths


map_dict, start, end, other_starts = convert_map_dict(input, str)
og_start_path = bfs(map_dict, start, end)[end]

path_list = [og_start_path]
for start in other_starts:
    path = bfs(map_dict, start, end)
    if end in path:
        path_list.append(path[end])


"""
Analysis of solution
Initially, I thought that the height was similar to the cost of the path, leading me to immediately consider dijkstra's
single source shortest path algorithm. However, after implementing it, there were some issues with the searching
that led it to fail on the actual input. This is likely due to the way dijkstra searches for the next edge and vertex
to run on.

After that, I realised that BFS was actually sufficient, the height was just to tell us whether or not that node was 
accessible from the current block, but it was still a single step. The BFS solution was able to solve it succinctly.

Time Complexity: O(N) Where N represents the number of vertices (Loop through each vertice and visit once)
Space Complexity: O(N) Where N represents the number of vertices (Store each vertices visited status and shortest path)
"""

print("Part 1: ", og_start_path)
print("Part 2: ", min(path_list))
