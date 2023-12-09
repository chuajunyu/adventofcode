import string
from utils import read_input_lines


input = read_input_lines("input.txt")

def part1(input):
    total = 0
    for line in input:
        line = line.strip(string.ascii_lowercase + string.ascii_uppercase)
        if (not line):
            continue
        num = line[0] + line[-1]
        total += int(num)
    return total


print(part1(input))


def part2(input):
    total = 0
    valid = "one,two,three,four,five,six,seven,eight,nine"
    valid_list = [s for s in valid.split(',')] + list(str(i) for i in range(10))
    valid = dict(zip(valid.split(','), range(1, 10)))
    for line in input:
        low = 1000000
        low_n = valid_list[0]
        for n in valid_list:
            index = line.find(n)
            if index < 0:
                continue
            
            if index < low:
                low = index
                low_n = n

        high = 100000000
        high_n = valid_list[0]
        for n in valid_list:
            index = line[::-1].find(n[::-1])
            
            if index < 0:
                continue
    
            if index < high:
                high = index
                high_n = n

        if low_n in valid:
            low_n = str(valid[low_n])

        if high_n in valid:
            high_n = str(valid[high_n])
        
        
        num = low_n + high_n
        total += int(num)

    return total


print(part2(input))

