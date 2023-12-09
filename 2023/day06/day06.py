from utils import read_input_lines

"""
Distance = time held down * (total time - time held down)

D = t * (T - t)

t * (T - t) > D
"""

input = read_input_lines("input.txt")


def get_time_and_dist(input):
    result = []
    for line in input:
        info = line.split(":")[1].strip()
        info = [int(i.strip()) for i in info.split(" ") if i]
        result.append(info)
    return result


def part1(input):
    time, dist = get_time_and_dist(input)
    total = 1
    for t, d in zip(time, dist):
        count = 0
        for i in range(t + 1):
            if (i * (t - i)) > d:
                count += 1
        total *= count
    return total


print(part1(input))


def part2(input):
    time, dist = get_time_and_dist(input)
    time = [str(t) for t in time]
    time = int("".join(time))
    dist = [str(d) for d in dist]
    dist = int("".join(dist))
    total = 0
    for t in range(time + 1):
        if (t * (time - t)) > dist:
            total += 1
    return total


print(part2(input))

