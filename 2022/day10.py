from tools import extract_input

input = extract_input(r"input10.txt")


def crt(input):
    cycle = 0
    x = 1
    output = 0

    to_add = 0
    prev_addx = False

    instructions = iter(input + ["noop"])

    break_next = False

    while True:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            output += cycle * x

        if prev_addx:
            x += to_add
            prev_addx = False

            if break_next:
                break
        else:
            if break_next:
                break

            line = next(instructions, False)

            if not line:
                break_next = True
                continue

            if 'addx' in line:
                _, amt = line.split(" ")
                amt = int(amt)
                prev_addx = True
                to_add = amt

    return output, cycle


def render_crt(input):
    cycle = 0
    x = 1
    output = ''

    to_add = 0
    prev_addx = False

    instructions = iter(input + ["noop"])

    break_next = False

    while True:
        cycle += 1
        if ((cycle % 40) - 1) in [x - 1, x, x + 1]:
            output += '#'
        else:
            output += '.'

        if cycle % 40 == 0:
            print(output)
            output = ''

        if prev_addx:
            x += to_add
            prev_addx = False

            if break_next:
                break
        else:
            if break_next:
                break

            line = next(instructions, False)

            if not line:
                break_next = True
                continue

            if 'addx' in line:
                _, amt = line.split(" ")
                amt = int(amt)
                prev_addx = True
                to_add = amt
    return


"""
Analysis of solution
- Quite repetitive, a better more well designed and concise solution probably exists

Time Complexity: O(N) -- One loop through the set of instructions
Space Complexity: O(1) -- Only saves data of current step/ fixed number of recent steps etc


Alternative Online Solution
Compute the values of X at each cycle and record them in a dictionary
- Saves the need for the extra flags to keep track of previous addx and when to add them in
- Can use the dictionary for part 2 as well, saving compute

Time Complextiy: O(N) -- One loop through the set of instructions (But reusing this result for part 2 makes it cleaner)
Space Complexity: O(N) -- Saves data of all the previously computed cycles
"""

print("Part 1: ", crt(input))
print("Part 2: ")
render_crt(input)
