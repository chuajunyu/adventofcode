from tools import extract_input

input = extract_input(r'input01.txt')


def find_highest_calories(input):
    highest = 0
    curr = 0
    for calories in input:
        if calories == '':
            if curr > highest:
                highest = curr
            curr = 0
        else:
            curr += int(calories)
    return highest


def find_calories_list(input):
    calories_list = list()
    curr = 0
    for calories in input:
        if calories == '':
            calories_list.append(curr)
            curr = 0
        else:
            curr += int(calories)
    return calories_list


calories_list = find_calories_list(input)
calories_list.sort(reverse=True)
top = calories_list[0]
top3 = sum(calories_list[:3])

print('Part 1: ', top)
print('Part 2: ', top3)
