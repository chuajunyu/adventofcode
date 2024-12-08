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
    

def part1_(input):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

    def dfs(x, y, to_find):
        if to_find == "":
            return 0
        
        count = 0

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
                continue
            
            if input[new_x][new_y] == to_find[0]:
                if len(to_find) == 1:
                    count += 1
                else:
                    count += dfs(new_x, new_y, to_find[1:])

        return count

    total = 0
    for x, line in enumerate(input):
        for y, letter in enumerate(line):
            if letter == "X":
                total += dfs(x, y, "MA")

    return total


def part1(input):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    to_find = "XMAS"
    count = 0
    for x, line in enumerate(input):
        for y, letter in enumerate(line):
            if letter == to_find[0]:
                for dx, dy in directions:
                    found = False
                    curr_x = x
                    curr_y = y
                    for char in to_find[1:]:
                        curr_x += dx
                        curr_y += dy

                        if curr_x< 0 or curr_x >= len(input) or curr_y < 0 or curr_y >= len(input[0]):
                            break
                        
                        next = input[curr_x][curr_y]
                        if next == char:
                            if char == to_find[-1]:
                                found = True
                                break
                            continue
                        else:
                            break
                    if found:
                        count += 1
    return count
    


def part2(input):
    count = 0
    for x, line in enumerate(input):
        for y, letter in enumerate(line):
            if letter == "A":
                if x + 1 < len(input) and x - 1 >= 0 and y + 1 < len(input[0]) and y - 1 >= 0:
                    if input[x + 1][y + 1] == "S" and input[x - 1][y - 1] == "M" or input[x - 1][y - 1] == "S" and input[x + 1][y + 1] == "M":
                        if input[x + 1][y - 1] == "S" and input[x - 1][y + 1] == "M" or input[x - 1][y + 1] == "S" and input[x + 1][y - 1] == "M":
                            count += 1
    return count

if __name__ == '__main__':
    test_input = extract_input('test.txt')
    input = extract_input('input.txt')

    # print(f"Test Part 1: {part1(test_input) == 18}")
    # print(f"Test Part 2: {part2(test_input) == 9}")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
