"""
Advent of Code 2020

Day 7
"""

from tools import extract_input

FILENAME = "input.txt"

input = extract_input(FILENAME)

class BagType:
    def __init__(self, rule):
        color, contains = rule.split('contain')  
        self.color = color[:color.index(' bags')]  # Remove ' bags', leaving only the color, e.g: 'shiny gold'
        contains = contains.split(',')
        self.contains = {}

        # Populate self.contains
        for bag in contains:
            if 'no other bags' in bag:
                break
            bag = bag[:bag.index(' bag')].strip()  # Remove ' bags'/' bag' and whitespace, e.g: '2 shiny gold'
            bagcolor = bag[2:]  # slices out the color, e.g.: 'shiny gold'
            bagnumber = int(bag[0])
            self.contains[bagcolor] = bagnumber

    def give_reference(self, bags):
        """
        Creates a attribute named self.bags, containing key value pairs of 
        bag instance to number of that type of bag. This is done according to
        self.contains.

        Params:
        bags: List of all the BagType instances specified in the rules(input)

        By having a reference to the real instances of the other BagTypes contained 
        within this BagType, it allows for easier implementation of search and sum,
        as the method can be called recursively on the references. 
        """
        self.bags = {}
        for bag in bags:
            if bag.color in self.contains:
                self.bags[bag] = self.contains[bag.color]

    def search(self, color):
        """
        Returns True if this bag contains a bag of a certain color, else False
        Checks recursively through the bags contained within it.
        """
        for bag in self.bags:
            if bag.color == color:
                return True
            else:
                if bag.search(color):
                    return True
        return False

    def sum(self):
        """
        Returns the number of bags contained within this bag. (Not including itself)
        Counts recursively through the bags contained within it.
        """
        sum = 0
        for bag in self.bags: 
            sum += (bag.sum() + 1) * self.bags[bag]  # Adds 1 to account for the bag itself.
        return sum
                
COLOR = 'shiny gold'

bags = []
for line in input:              # According to each line of the rules
    bags.append(BagType(line))  # Create a BagType object, append it to a list

for bag in bags:
    bag.give_reference(bags) 

# Part 1
count = 0
for bag in bags:
    if bag.search(COLOR):
        count += 1
print('Part 1: ', count)

# Part 2
for bag in bags:
    if bag.color == COLOR:
        print('Part 2: ', bag.sum())

# Answers: 257, 1038
