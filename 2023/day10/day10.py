from utils import read_input_lines

input = read_input_lines("input.txt")


def make_adjacency_list(input):
    adj_list = {}
    s = None
    h = len(input)
    w = len(input[0])
    for x, line in enumerate(input):
        for y, pipe in enumerate(line):
            neighbours = []
            if pipe == '-':
                neighbours = [(x, y - 1), (x, y + 1)]
            elif pipe == '|':
                neighbours = [(x - 1, y), (x + 1, y)]
            elif pipe == 'J':
                neighbours = [(x - 1, y), (x, y - 1)]
            elif pipe == 'F':
                neighbours = [(x + 1, y), (x, y + 1)]
            elif pipe == 'L':
                neighbours = [(x - 1, y), (x, y + 1)]
            elif pipe == '7':
                neighbours = [(x + 1, y), (x, y - 1)]
            elif pipe == 'S':
                s = (x, y)
                continue
            neighbours = [n for n in neighbours if 0 <= n[0] < h and 0 <= n[1] < w]
            if neighbours:
                adj_list[(x, y)] = neighbours

    # find the neighbours around s
    for coord in [(x, y) for x in range(s[0] - 1, s[0] + 2) for y in range(s[1] - 1, s[1] + 2)]:
        if s in adj_list.get(coord, []):
            adj_list[s] = adj_list.get(s, []) + [coord]
    return s, adj_list

def make_find_cycle():
    cache = [0]
    def find_cycle(s, adj_list):
        if cache[0]:
            return cache[0]
        visited = [s]
        stack = [adj_list[s][0]]
        while stack:
            curr = stack.pop(-1)
            visited.append(curr)
            for node in adj_list.get(curr, []):
                if node not in visited:
                    stack.append(node)
        cache[0] = visited
        return visited
    return find_cycle

find_cycle = make_find_cycle()


def part1(input):
    s, adj_list = make_adjacency_list(input)
    num = len(find_cycle(s, adj_list))
    return (num + 1) // 2


print(part1(input))
 

def part2(input):
    s, adj_list = make_adjacency_list(input)
    cycle = find_cycle(s, adj_list)
    count = 0
    for x, line in enumerate(input):
        is_outside = True
        prev_elem = ''
        for y, elem in enumerate(line):
            if (x, y) in cycle:
                if elem == 'S':  # Hardcoded this
                    elem = '|'

                if elem == '|':
                    is_outside = not is_outside
                else:
                    pattern = prev_elem + elem
                    # Crossed
                    if pattern in ['L7', 'FJ']:
                        is_outside = not is_outside
                        prev_elem = ''
                        continue
                    # Skimmed
                    elif pattern in ['LJ', 'F7']:
                        prev_elem = ''
                        continue
                    
                    if elem in 'LFJ7':
                        prev_elem = elem
            else:
                if not is_outside:
                    count += 1
    return count


print(part2(input))

