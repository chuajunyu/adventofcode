from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)

input = input[0].split(',')
input = [int(i) for i in input]

# Using a dictionary is much more efficient as it
# 1. Eliminates the need for iteration over huge lists
# 2. Has constant insertion/lookup vs append which is slow with large lists

input_dict = {}  
for i in input:
    if i in input_dict:
        input_dict[i] += 1
    else:
        input_dict[i] = 1


def simulate(state, days):
    for _ in range(days):
        new_state = {i:0 for i in range(9)}
        for days in state:
            if days == 0:
                new_state[8] += state[days]
                new_state[6] += state[days]
            else:
                new_state[days - 1] += state[days]
        state = new_state
    
    sum = 0
    for days in state:
        sum += state[days]
    return sum


print("Part 1: ", simulate(input_dict, 80))
print("Part 2: ",simulate(input_dict, 256))
