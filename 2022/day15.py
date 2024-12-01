from collections import defaultdict

from tools import extract_input


input = extract_input(r"input15.txt")


def get_manhattan_dist(point1, point2):
    p1x, p1y = point1
    p2x, p2y = point2
    return abs(p2x - p1x) + abs(p2y - p1y)


def extract_coordinates(coord_string):
    x_info, y_info = coord_string.split(', ')
    _, x = x_info.split("=")
    x = int(x)
    _, y = y_info.split("=")
    y = int(y)
    return x, y


def generate_map(input):
    cave_map = defaultdict(list)
    beacon_set = set()
    num_beacons = defaultdict(int)
    for line in input:
        sensor_info, beacon_info = line.split(":")
        _, sensor_info = sensor_info.split(' at ')
        _, beacon_info = beacon_info.split(' at ')
        sensor_coordinates = extract_coordinates(sensor_info)
        beacon_coordinates = extract_coordinates(beacon_info)
        dist = get_manhattan_dist(sensor_coordinates, beacon_coordinates)

        if beacon_coordinates not in beacon_set:
            beacon_set.add(beacon_coordinates)
            num_beacons[beacon_coordinates[1]] += 1

        sensor_x, sensor_y = sensor_coordinates
        for y_offset in range(dist + 1):
            if sensor_y + y_offset == sensor_y - y_offset:  # don't double append if y offset is 0
                start = sensor_x - dist + y_offset
                end = sensor_x + dist - y_offset
                cave_map[sensor_y + y_offset].append([start, 
                           end])
            else:
                cave_map[sensor_y + y_offset].append([sensor_x - dist + y_offset, 
                                                     sensor_x + dist - y_offset])
                cave_map[sensor_y - y_offset].append([sensor_x - dist + y_offset, 
                                                     sensor_x + dist - y_offset])
                
    return cave_map, num_beacons


def is_range_overlap(range1, range2):
    start1, stop1 = range1
    start2, stop2 = range2
    if stop1 >= start2 and stop2 >= start1:
        return True
    else:
        return False


def merge(ranges):
    starts = [r[0] for r in ranges]
    stops = [r[1] for r in ranges]
    output = [min(starts), max(stops)]
    return output


def merge_ranges(ranges):
    new_ranges = list(ranges)
    
    all_merges_complete = False
    while not all_merges_complete:
        ranges = new_ranges
        new_ranges = list()
        all_merges_complete = True

        already_merged = list()
        for i1, range1 in enumerate(ranges):
            to_merge = [range1]
            if i1 in already_merged:
                continue
            for i2, range2 in enumerate(ranges):
                if i1 == i2 or i2 in already_merged:
                    continue
                elif is_range_overlap(range1, range2):
                    to_merge.append(range2)
                    already_merged.append(i2)
                    all_merges_complete = False
            
            new_ranges.append(merge(to_merge))
    return new_ranges


def count_invalid_positions(cave_map, num_beacons, row):
    cave_row = cave_map[row]
    new_ranges = merge_ranges(cave_row)

    length = 0
    for line_range in new_ranges:
        start, stop = line_range
        length += stop - start + 1

    return length - num_beacons[row]


def find_free_space(cave_map, limits):
    for y in range(3, limits):
        cave_row = cave_map[y]
        new_ranges = merge_ranges(cave_row)
        for line_range in new_ranges:
            start, stop = line_range
            if start <= 0 and stop < limits:
                print(4000000 * (stop + 1) + y)


cave_map, num_beacons = generate_map(input)
print(count_invalid_positions(cave_map, num_beacons, 2000000))
print(find_free_space(cave_map, 4000000))
