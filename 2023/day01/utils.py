def read_input_lines(filename):
    with open(filename) as file:
        res = [line.strip('\n') for line in file.readlines()]
    return res
