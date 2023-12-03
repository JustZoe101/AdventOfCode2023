#tried:
#54927 answer

import re

f = open("day1/input.txt")
INPUT = f.readlines()

total = 0

for i in INPUT:
    numbers = re.findall("([\d]+)", i)
    print(numbers)
    
    print(numbers[0][0] + numbers[-1:][0][-1:])
    total += int(numbers[0][0] + numbers[-1:][0][-1:])

print("Total: ", total)