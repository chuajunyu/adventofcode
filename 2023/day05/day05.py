from utils import read_input_lines

input = read_input_lines("input.txt")

def split_to_groups(input):
    # split up input into the groups
    groups = []
    curr = []
    for line in input:
        if line == "":
            groups.append(curr)
            curr = []
        else:
            curr.append(line)
    groups.append(curr)
    return groups

def extract_map(groups):
    seeds, maps = groups[0], groups[1:]
    
    seeds = seeds[0].split(": ")[1].strip().split(" ")
    seeds = [int(s) for s in seeds]

    final_maps = {}
    for map_id, mapy in enumerate(maps):
        local_map = []
        map_content = mapy[1:]
        
        
        for line in map_content:
            source, dest, ran = line.strip().split()
            local_map.append((int(source), int(dest), int(ran)))
        final_maps[map_id] = local_map

    return seeds, final_maps



def mapper(input_list, map_info):
    result = []
    for (x, i) in input_list:
        found = False
        for info in map_info:
            dest, source, ran = info
            if source <= i <= source + ran:
                i_result = dest + i - source
                result.append((x, i_result))
                found = True
                break
        if not found:
            result.append((x, i))
    return result
        


def part1(input):
    seeds, final_map = extract_map(split_to_groups(input))

    temp = [(i, i) for i in seeds]
    for map_id in final_map:
        map_info = final_map[map_id]

        temp = mapper(temp, map_info)
    loc = [y for (x, y) in temp]
    return min(loc)


print(part1(input))
    
import time
def mapper2(input_list, map_info):
    result = []
    while input_list:
        # time.sleep(1)
        # print(input_list)
        # print("result: ", result)
        
        (start, end) = input_list.pop(0)
        found = False
        for info in map_info:
            dest, source, ran = info
            source_end = source + ran - 1
            dest_end = dest + ran - 1

            # if start of seed is within the source range
            if source <= start <= source_end:

                # if the end of seed exceed source range
                if end > source_end:
                    result.append((dest + (start - source), dest_end))
                    input_list.append((source_end + 1, end))
                else:
                    result.append((dest + (start - source), dest + (start - source) + (end - start)))
                found = True
                break

            # If the end is within source range
            if source <= end <= source_end:
                result.append((dest, dest + (end - source)))
                input_list.append((start, source - 1))
                found = True
                break

            # if the source is within range of seed
            if start < source <= source_end < end:
                result.append((dest, dest_end))
                input_list.append((start, source - 1))
                input_list.append((source_end + 1, end))
                found = True
                break

        if not found:
            result.append((start, end))
    return result


def part2(input):
    seeds, final_map = extract_map(split_to_groups(input))

    odds = [s for i, s in enumerate(seeds) if (i + 1) % 2]
    evens = [s for i, s in enumerate(seeds) if i % 2]

    seeds = []
    for (start, ran) in zip(odds, evens):
        seeds.append((start, start + ran - 1))


    # temp = [(i, i) for i in seeds]
    for map_id in final_map:
        map_info = final_map[map_id]

        seeds = mapper2(seeds, map_info)
    loc = [x for (x, y) in seeds]

    return min(loc)

print(part2(input))
