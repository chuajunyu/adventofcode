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
  
    
def parse_dependencies(deps):
    dep_dict = {}
    for dep in deps:
        x, y = dep.split("|")
        x = int(x)
        y = int(y)
        curr_y = dep_dict.get(y, [])
        curr_y.append(x)
        dep_dict[y] = curr_y
    return dep_dict


def check_order(update, deps):
    for i, page in enumerate(update):
        page_deps = deps.get(page, [])

        after = update[i + 1:]

        if not all(x not in page_deps for x in after):
            return False
    return True


def part1(input):
    partition = input.index('')
    deps = input[:partition]
    updates = input[partition+1:]

    deps = parse_dependencies(deps)

    ordered = []
    for update in updates:
        update = [int(x) for x in update.split(',')]
        if check_order(update, deps):
            ordered.append(update)

    total = 0
    for update in ordered:
        total += update[(len(update) // 2)]
    
    return total


def part2(input):
    partition = input.index('')
    deps = input[:partition]
    updates = input[partition+1:]

    deps = parse_dependencies(deps)

    notOrdered = []
    for update in updates:
        update = [int(x) for x in update.split(',')]
        if not check_order(update, deps):
            notOrdered.append(update)
    
    new_updates = []
    for update in notOrdered:
        new = update
        tmp = []
        while not check_order(new, deps):
            for i, page in enumerate(new):
                page_deps = deps.get(page, [])

                after = new[i + 1:]
                should_be_before = [x for x in after if x in page_deps]

                for x in should_be_before:
                    tmp.append(x)
                    
                if should_be_before:
                    tmp.append(page)
                    tmp.extend([x for x in after if x not in should_be_before])
                    break
                else:
                    tmp.append(page)

            new = tmp
            tmp = []
        new_updates.append(new)

    total = 0
    for update in new_updates:
        total += update[(len(update) // 2)]

    return total


if __name__ == '__main__':
    test_input = extract_input('test.txt')
    input = extract_input('input.txt')

    # print(f"Test Part 1: {part1(test_input) == 143}")
    # print(f"Test Part 2: {part2(test_input) == 123}")

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
