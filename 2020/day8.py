"""
AOC 2020

Day 8
"""

from tools import extract_input

FILENAME = 'input.txt'

input = extract_input(FILENAME)

# Part 1

def make_intepreter(input):
    """
    Returns a recursive intepret function, which stops after the first iteration of a loop

    Purpose of using a higher order function is to create a mutable function
    with a local frame where the local variables accumulator and readlines set 
    can be accessed and changes can be saved (like a cache)
    """
    accumulator = 0
    readlines = set()  # If line number appears in here, the code is looping

    def intepret(line_number=0):
        """
        Inteprets the line specified by the line_number argument, recursively calls
        intepret on the next line to be intepreted.

        If there is an infinite loop:
        Return: Accumulator value at the end of the first loop, True

        If no infinite loop
        Return: Accumulator value after the last line is ran, False
        """
        
        nonlocal accumulator

        if line_number in readlines:
            return accumulator, True  # Line has been read before, infinite loop
        else:
            readlines.add(line_number)
        
        # If IndexError is raised due to out of range, then we know that the end
        # of the input was reached and there was no infinite loop
        try:
            operation, arg = input[line_number].split(' ')  
        except: 
            return accumulator, False
        
        if operation == 'acc':
            accumulator += int(arg)
            return intepret(line_number + 1)
        elif operation == 'jmp':
            return intepret(line_number + int(arg))
        elif operation == 'nop':
            return intepret(line_number + 1)

    return intepret

intepreter = make_intepreter(input)
accumulator_value = intepreter()[0]

print('Part 1: ', accumulator_value)


# Part 2

def brute_force(input):
    """
    Loops through the input, for each line with jmp or nop, create a copy of input
    with the operation of that line swapped to nop and jmp respectively.

    Run make_intepreter on that new input and call function returned.
    If the returned bool is True: Infinite loop detected, continue testing
    Else returned bool is False: Infinite loop stopped, return accumulator 
    """
    for i in range(len(input)):
        operation, arg = input[i].split(' ')
        if operation == 'nop':
            new_input = list(input)
            new_input[i] = 'jmp ' + arg
        elif operation == 'jmp':
            new_input = list(input)
            new_input[i] = 'nop ' + arg
        else:
            continue

        intepreter = make_intepreter(new_input)
        accum, infinite_loop = intepreter()
        if not infinite_loop:
            return accum

accumulator_value_2 = brute_force(input)
print('Part 2: ', accumulator_value_2)

# Answers: 1594, 758
