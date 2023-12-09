from utils import read_input_lines

input = read_input_lines("input.txt")


def extract_instructions_and_graph(input):
    RL_instructions = input[0]
    graph_info = input[2:]
    graph = dict()
    for node in graph_info:
        head, branches = node.strip().split(" = ")
        graph[head] = tuple(branches.strip("()").split(", "))
    return RL_instructions, graph


def memoise(func):
    cache = {}
    def memoised_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoised_func

@memoise
def lookup(instruction, curr):
    if instruction == 'R':
        return graph[curr][1]
    elif instruction == 'L':
        return graph[curr][0]

@memoise
def step(RL_instructions, curr):
    for i in RL_instructions:
        curr = lookup(i, curr)
    return curr


RL_instructions, graph = extract_instructions_and_graph(input)


def part1(input):
    RL_instructions, graph = extract_instructions_and_graph(input)
    instruction_length = len(RL_instructions)
    count = 0
    curr = 'AAA'
    while not curr == 'ZZZ':
        curr = step(RL_instructions, curr)
        count += instruction_length
    return count


print(part1(input))


from math import lcm


def part2(input):
    RL_instructions, graph = extract_instructions_and_graph(input)
    instruction_length = len(RL_instructions)
    count = 0
    curr_list = list(filter(lambda key: key[-1] == 'A', graph.keys()))
    count_list = []
    for curr in curr_list:
        c = 0
        while not curr[-1] == 'Z':
            curr = step(RL_instructions, curr)
            c += instruction_length
        count_list.append(c)
    return lcm(*count_list)


print(part2(input))

