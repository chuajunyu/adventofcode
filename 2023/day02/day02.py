from utils import read_input_lines

input = read_input_lines("input.txt")


def parse_line(line):
    """
    Turn the line into a lists of lists of 
    [[R,G,B], [R,G,B], [R,G,B]]
    """
    game_info = []
    list_of_cube_sets = line.split(";")
    for cube_set in list_of_cube_sets:
        set_info = [0] * 3
        list_of_colors = cube_set.strip().split(",")
        for info in list_of_colors:
            num, color = info.strip().split(" ")
            if color == "red":
                set_info[0] = int(num)
            elif color == "green":
                set_info[1] = int(num)
            elif color == "blue":
                set_info[2] = int(num)
        game_info.append(set_info)
    return game_info


def part1(input):
    total = 0
    for line in input:
        line_head, line_tail = line.split(":")
        game_info = parse_line(line_tail)
        game_id = int(line_head.strip("Game "))
        
        impossible = False
        for game in game_info:
            r, g, b = game
            if r > 12 or g > 13 or b > 14:
                impossible = True
                break

        if not impossible:
            total += game_id
    return total


print(part1(input))


def part2(input):
    total = 0
    for line in input:
        line_head, line_tail = line.split(":")
        game_info = parse_line(line_tail)
        game_id = int(line_head.strip("Game "))

        max_red = max([cube_set[0] for cube_set in game_info])
        max_green = max([cube_set[1] for cube_set in game_info])
        max_blue = max([cube_set[2] for cube_set in game_info])

        total += max_red * max_green * max_blue
    return total


print(part2(input))

