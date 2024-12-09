def extract_input(filename):
    """
    Reads a text file into a list of strings, where each string corresponds
    to a line in the text file.

    Removes the trailing newline at the end of each string.
    """
    with open(filename) as file:
        input = file.read()

    return input.strip()


def read_filesystem(input):
    filesystem = []
    curr_idx = 0
    is_free = False
    for char in input:
        if is_free:
            filesystem.append([-1, int(char), is_free])
        else:
            filesystem.append([curr_idx, int(char), is_free])
            curr_idx += 1
        is_free = not is_free
    return filesystem


def part1(input):
    fs = read_filesystem(input)
    ptr1 = 0
    ptr2 = len(fs) - 1

    while ptr1 < ptr2:
        # Advance ptr1 to the next free space
        while not fs[ptr1][2]:
            ptr1 += 1

        # Advance ptr2 to the next used space
        while fs[ptr2][2]:
            ptr2 -= 1

        # If ptr 1 has advanced past ptr2, break
        if ptr1 > ptr2:
            break

        # Perform a swap
        free_size = fs[ptr1][1]
        used_size = fs[ptr2][1]

        if free_size > used_size:
            fs[ptr1][0] = fs[ptr2][0]  # Swap IDs
            fs[ptr2][0] = -1 
            fs[ptr1][2] = False
            fs[ptr2][2] = True
            fs.insert(ptr1 + 1, [fs[ptr1][0], free_size - used_size, True])
            fs[ptr1][1] = used_size
        elif used_size > free_size:
            fs[ptr1][0] = fs[ptr2][0]  # Swap IDs
            fs[ptr1][2] = False
            fs[ptr2][2] = True
            fs.insert(ptr2, [fs[ptr2][0], used_size - free_size, False])
            ptr2 += 1
            fs[ptr2][0] = -1
            fs[ptr2][1] = free_size
        else:
            fs[ptr1][0] = fs[ptr2][0]  # Swap IDs
            fs[ptr2][0] = -1
            fs[ptr1][2] = False
            fs[ptr2][2] = True

    return calculate_checksum(fs)


def visualize(fs):
    for block in fs:
        if not block[2]:
            print(f"{str(block[0]) * block[1]}", end="")
        else:
            print(f"{'.' * block[1]}", end="")
    print()


def calculate_checksum(fs):
    checksum = 0
    curr_idx = 0
    for block in fs:
        id, length, is_free = block
        if id == -1 and is_free:
            curr_idx += length
            continue
        
        start = curr_idx
        end = curr_idx + length - 1

        checksum += (((start + end) * length) // 2) * id

        curr_idx += length

    return checksum


def part2(input):
    fs = read_filesystem(input)
    ptr2 = len(fs) - 1

    last_id = len(input) // 2

    while ptr2 > 0:
        # Advance ptr2 to the next used space
        while fs[ptr2][2]:
            ptr2 -= 1
        
        if ptr2 == 0:
            break

        id, used_size, is_free = fs[ptr2]

        if not id == last_id:
            ptr2 -= 1
            continue
        else:
            last_id -= 1

        # Find a free block of size >= length
        ptr1 = 0
        found = False
        while ptr1 < ptr2:
            _, free_size, is_free = fs[ptr1]
            if is_free and free_size >= used_size:
                found = True
                break
            ptr1 += 1

        if not found:
            ptr2 -= 1
            continue

        if free_size > used_size:
            fs[ptr1][0] = fs[ptr2][0]  # Swap IDs
            fs[ptr2][0] = -1 
            fs[ptr1][2] = False
            fs[ptr2][2] = True
            fs.insert(ptr1 + 1, [-1, free_size - used_size, True])
            fs[ptr1][1] = used_size
        else:
            fs[ptr1][0] = fs[ptr2][0]  # Swap IDs
            fs[ptr2][0] = -1
            fs[ptr1][2] = False
            fs[ptr2][2] = True

    return calculate_checksum(fs)


if __name__ == "__main__":
    input = extract_input("input.txt")
    test_input = extract_input("test.txt")

    # print(part1(test_input))  # Should be 1928
    # print(part2(test_input))  # Should be 2858

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
