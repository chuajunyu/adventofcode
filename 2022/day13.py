from tools import read_all

input = read_all(r"input13.txt")


def is_valid_pair(left, right):
    for i, left_ele in enumerate(left):
        if len(right) == i:
            return False
        right_ele = right[i]

        if type(left_ele) == int and type(right_ele) == int:
            if left_ele < right_ele:
                return True
            elif left_ele > right_ele:
                return False

        elif type(left_ele) == list and type(right_ele) == list:
            result = is_valid_pair(left_ele, right_ele)
            if result is True:
                return True
            elif result is False:
                return False

        else:
            if type(left_ele) != list:
                left_ele = [left_ele]
            if type(right_ele) != list:
                right_ele = [right_ele]
            
            result = is_valid_pair(left_ele, right_ele)
            if result is True:
                return True
            elif result is False:
                return False

    if len(left) < len(right):
        return True
    elif len(left) == len(right):
        return
                    

def count_valid_pairs(input):
    input = input.split('\n\n')
    count = 0
    for i, pair in enumerate(input, 1):
        pair.strip('\n ')
        left, right = pair.split('\n')
        left = eval(left)
        right = eval(right)
        if is_valid_pair(left, right):
            count += i

    return count


def merge_sort(input):
    length = len(input)
    if length == 1:
        return input
    half = length // 2
    left = input[:half]
    right = input[half:]

    left = merge_sort(left)
    right = merge_sort(right)

    sorted_list = list()
    left_pointer = 0
    right_pointer = 0

    while True:
        if left_pointer >= len(left):
            sorted_list.extend(right[right_pointer:])
            break
        if right_pointer >= len(right):
            sorted_list.extend(left[left_pointer:])
            break
        
        if is_valid_pair(left[left_pointer], right[right_pointer]) is True:
            sorted_list.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right[right_pointer])
            right_pointer += 1
    return sorted_list


def calculate_decoder_key(input):
    input = [eval(line) for line in input.split('\n') if line != ''] + [[[2]], [[6]]]
    sorted_list = merge_sort(input)
    divider_1 = sorted_list.index([[2]]) + 1
    divider_2 = sorted_list.index([[6]]) + 1
    return divider_1 * divider_2

    


print("Part 1: ", count_valid_pairs(input))
print("Part 2: ", calculate_decoder_key(input))
    