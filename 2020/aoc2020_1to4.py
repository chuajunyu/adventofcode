"""
Advent of Code 2020
Days 1-4
"""

with open("input.txt") as file:
    input = file.readlines()

# To remove the newline    
for i in range(len(input)):
    input[i] = input[i].strip('\n')

# Day 1

def convert_list(input):
    list = input.split('\n')
    return list

def find_mul_2020(input):
    nums = convert_list(input)
    for x in nums:
        for y in nums:
            for z in nums:
                if int(x) + int(y) + int(z) == 2020:
                    return int(x)*int(y)*int(z)

# Answers: 1019571, 100655544


# Day 2

from os import name
import re

def check_valid(input):
    creds = convert_list(input)
    valid = 0
    for cred in creds:
        m = re.search(r"(\d+)-(\d+)\s(.):\s(.+)", cred)
        lower, upper, char, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        count = 0
        for c in password:
            if c == char:
                count += 1
        if lower <= count <= upper:
            valid += 1
    return valid


def check_new_valid(input):
    creds = convert_list(input)
    valid = 0
    for cred in creds:
        m = re.search(r"(\d+)-(\d+)\s(.):\s(.+)", cred)
        lower, upper, char, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        if password[lower-1] == char and not password[upper-1] == char:
                valid += 1
        elif not password[lower-1] == char and password[upper-1] == char:
            valid += 1
    return valid

# Answers: 607, 321


# Day 3

def count_trees(input, right, down):
    height = len(input)
    width = len(input[0])
    y, x = 0, 0
    trees = 0
    while y + down < height:
        y, x = y + down, (x + right) % (width)
        if input[y][x] == '#':
            trees += 1
    return trees

# slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# trees = [count_trees(input, *slope) for slope in slopes]

def mul(list):
    mul = 1
    for i in list:
        mul *= i
    return mul

# Answers: 203, 3316272960


# Day 4

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

valid_passport_set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def convert_passport(input):
    """
    Function to convert list of strings raw input to segregated passports
    """
    passports = []
    curr = {}
    
    for line in input:
        if not line:  # Blank line signifying end of passport
            passports.append(curr)
            curr = {}
            continue
        else:
            datalist = line.split()
            for data in datalist:
                match = re.search(r'(\w{3}):(.*)', data)
                curr[match.group(1)] = match.group(2)
    passports.append(curr)
    return passports


def check_field_valid(passport):
    check = []
    
    check.append(1920 <= int(passport['byr']) <= 2002)
    check.append(2010 <= int(passport['iyr']) <= 2020)
    check.append(2020 <= int(passport['eyr']) <= 2030)

    if 'cm' in passport['hgt']:
        check.append(150 <= int(passport['hgt'][:-2]) <= 193)
    elif 'in' in passport['hgt']:
        check.append(59 <= int(passport['hgt'][:-2]) <= 76)
    else:
        check.append(False)

    check.append(bool(re.search(r'#[a-f0-9]{6}', passport['hcl'])))

    check.append(passport['ecl'] in valid_ecl)

    check.append(len(passport['pid']) == 9 and passport['pid'].isdecimal())

    return all(check)


def count_valid_passports(input):
    passports = convert_passport(input)
    valid = 0

    for passport in passports:
        present, allvalid = False, False
        field_set = set([field for field in passport])
        if valid_passport_set.issubset(field_set):
            present = True
            allvalid = check_field_valid(passport)

        if present and allvalid:
            valid += 1
    return valid

# Answers: 237, 172
