from tools import read_all

input = read_all(r"input06.txt")

def find_marker(num_distinct):
    for i in range(num_distinct, len(input) + 1):
        current_window = input[i-num_distinct:i]
        if len(set(current_window)) == num_distinct:
            return i


print("Part 1: ", find_marker(4))
print("Part 2: ", find_marker(14))
