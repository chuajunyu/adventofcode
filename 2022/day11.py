from tools import read_all
from time import time

input = read_all(r"input11.txt")


class Monkey:
    def __init__(self, info, monkey_dict):
        _, item_info = info[0].split(":")
        self.items = [int(num.strip()) for num in item_info.split(',')]

        _, inspect_info = info[1].split(":")
        _, self.inspect_formula = inspect_info.split("=")

        _, divisible_factor = info[2].split('by ')
        self.test_num = int(divisible_factor)

        _, true_monkey = info[3].split('monkey ')
        self.true_monkey = int(true_monkey)

        _, false_monkey = info[4].split('monkey ')
        self.false_monkey = int(false_monkey)

        self.monkey_dict = monkey_dict
        self.inspect_counter = 0

    def execute_turn(self, divide_3):
        while self.items:
            worry_level = self.items.pop(0)
            worry_level = self.inspect(worry_level)
            
            if divide_3:
                worry_level //= 3
            else:
                worry_level %= 9699690  # LCM of all the test nums/divisible test factors

            if worry_level % self.test_num == 0:
                self.monkey_dict[self.true_monkey].items.append(worry_level)
            else:
                self.monkey_dict[self.false_monkey].items.append(worry_level)

    def inspect(self, old):
        new = eval(self.inspect_formula)
        self.inspect_counter += 1
        return new


def load_monkeys(input):
    monkey_dict = dict()
    monkey_list = input.split('\n\n')
    for i, monkey_info in enumerate(monkey_list):
        monkey_info = monkey_info.split('\n')
        monkey = Monkey(monkey_info[1:], monkey_dict)
        monkey_dict[i] = monkey
    return monkey_dict


def play_round(monkey_dict, divide_3):
    for monkey in monkey_dict:
        monkey_dict[monkey].execute_turn(divide_3)


def calculate_monkey_business(input, num_rounds, divide_3):
    monkey_dict = load_monkeys(input)
    for _ in range(num_rounds):
        play_round(monkey_dict, divide_3)

    monkey_business_list = list()
    for monkey in monkey_dict:
        monkey_business_list.append(monkey_dict[monkey].inspect_counter)

    monkey_business_list.sort(reverse=True)
    print(monkey_business_list)

    return monkey_business_list[0] * monkey_business_list[1]


"""
Analysis of solution
Part 1:
- Due to the complex nature of the problem, I decided to break it down through OOP and functional abstraction.
- The Monkey class will take care of all the calculations done by the monkey during it's turn
- Functions that loop through the Monkeys and call them to execute each round is called

Part 2:
- Seemed easy at first glance, however, the worry levels started to increase and the integer operations took too long
- Had to figure out to use modulo LCM in order to keep the computations within time

Time Complexity:
O(N) where N = number of items * rounds

Space Complexity:
O(N) where N = number of monkeys 
"""

print("Part 1: ", calculate_monkey_business(input, 20, divide_3=True))
print("Part 2: ", calculate_monkey_business(input, 10000, divide_3=False))
