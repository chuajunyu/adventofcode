from tools import extract_input


input = extract_input(r"input04.txt")

total = 0
for pair in input:
    elf1, elf2 = pair.split(',')
    start1, stop1 = elf1.split('-')
    start1, stop1 = int(start1), int(stop1)
    start2, stop2 = elf2.split('-')
    start2, stop2 = int(start2), int(stop2)

    if start1 >= start2 and stop1 <= stop2 or start2 >= start1 and stop2 <= stop1:
        total += 1

print(total)


total = 0
for pair in input:
    elf1, elf2 = pair.split(',')
    start1, stop1 = elf1.split('-')
    start1, stop1 = int(start1), int(stop1)
    start2, stop2 = elf2.split('-')
    start2, stop2 = int(start2), int(stop2)

    if stop1 >= start2 and stop2 >= start1:
        total += 1

print(total)