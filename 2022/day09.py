from tools import extract_input

input = extract_input(r"input09.txt")


def get_neighbours(coordinate):
    x, y = coordinate
    neighbour_list = list()
    for nbx in range(x-1, x+2):
        for nby in range(y-1, y+2):
            neighbour_list.append((nbx,nby))
    return neighbour_list


def catch_up_step(old_head, new_head, tail):
    neighbours = get_neighbours(new_head)
    if tail in neighbours:
        # print('no', tail, tail)
        return new_head, tail
    else:
        # When the prev node is directly in line with the current node, just move to it
        if new_head[0] == tail[0] or new_head[1] == tail[1]:  
            new_tail = (new_head[0] + tail[0]) // 2, (new_head[1] + tail[1]) // 2
            return new_head, new_tail

        # If the prev node moved diagonally out of line with the current node, move diagonally to join behind it
        delta_x = new_head[0] - old_head[0]
        delta_y = new_head[1] - old_head[1]
        if abs(delta_x) + abs(delta_y) == 2:
            new_tail = tail[0] + delta_x, tail[1] + delta_y
            return new_head, new_tail

        return new_head, old_head


def execute_step(head, tail, direction):
    head_x, head_y = head
    if direction == 'U':
        new_head = head_x, head_y + 1
    elif direction == 'D':
        new_head = head_x, head_y - 1
    elif direction == 'L':
        new_head = head_x - 1, head_y
    elif direction == 'R':
        new_head = head_x + 1, head_y
    return new_head, tail


def calculate_visited(input):
    visited = [(0, 0)]
    head = (0, 0)
    tail = (0, 0)
    
    for line in input:
        direction, num = line.split(' ')
        for _ in range(int(num)):
            new_head, tail = execute_step(head, tail, direction)
            head, tail = catch_up_step(head, new_head, tail)

            if tail not in visited:
                visited.append(tail)
    
    return len(visited)


def calculate_visited_long(input, tail_length):
    visited = [(0, 0)]
    head = (0, 0)
    tails = [(0, 0)] * tail_length

    for line in input:
        direction, num = line.split(' ')
        for _ in range(int(num)):
            new_head, tails[0] = execute_step(head, tails[0], direction)

            new_tails = list(tails)
            for i, tail in enumerate(tails):
                if i == 0:
                    head, new_tails[i] = catch_up_step(head, new_head, tail)
                else:
                    _, new_tails[i] = catch_up_step(tails[i-1], new_tails[i-1], tail)
            
            tails = new_tails

            if tails[-1] not in visited:
                visited.append(tails[-1])

    return len(visited)


print("Part 1 (Original Solution): ", calculate_visited(input))
print("Part 1 (Scalable): ", calculate_visited_long(input, 1))
print("Part 2 : ", calculate_visited_long(input, 9))
