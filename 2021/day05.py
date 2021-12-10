from tools import extract_input

FILENAME = "input.txt"
raw_input = extract_input(FILENAME)

# Converts string "x1, y1 -> x2, y2" to list of ints [x1, y1, x2, y2]
input = []  
for line in raw_input:
    new_line = []
    coords = line.split('->')
    for coord in coords:
        [new_line.append(int(num)) for num in coord.split(',')]
    input.append(new_line)


def keep_hor_and_ver(input):
    """
    Keeps only lines where x1 = x2 or y1 = y2
    """
    filtered_input = []
    for line in input:
        if line[0] == line[2]:
            filtered_input.append(line)
        elif line[1] == line[3]:
            filtered_input.append(line)
    return filtered_input


def find_overlap(input):
    """
    Returns the number of points where there is an overlap of lines
    """
    points = {}
    for line in input:
        x1, y1, x2, y2 = line
        coords = None

        if x1 == x2:
            min, max = sorted([y1, y2])
            coords = [(x1, y) for y in range(min, max + 1)]  # Note use of tuple (immutable)
        elif y1 == y2:
            min, max = sorted([x1, x2])
            coords = [(x, y1) for x in range(min, max + 1)]  # Dict keys must be immutable

        else:  # Diagonal Lines
            xdir = (x2 - x1) // abs(x2 - x1)  # Calculating step of range for x coords
            ydir = (y2 - y1) // abs(y2 - y1)  # Calculating step of range for y coords
            coords = [(x, y) for x, y 
                       in zip(range(x1, x2 + xdir, xdir),
                       range(y1, y2 + ydir, ydir))]

        if coords:
            for coord in coords:
                if coord in points:
                    points[coord] += 1
                else:
                    points[coord] = 1

    overlap = [coord for coord in points if points[coord] >= 2]
    return len(overlap)


filtered = keep_hor_and_ver(input)  # Input with only horizontal or vertical lines
print("Part 1: ", find_overlap(filtered))
print("Part 2: ", find_overlap(input))
