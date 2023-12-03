#tried:
#525911 answer

import re

f = open("day3/input.txt")

SPECCHARS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "/", "|", "\\"]
LINES = f.read().split("\n")
MATRIX = []

sum = 0

for lineindex, line in enumerate(LINES):
    line = "." + line + "."
    numbers = re.findall("(\d+)", line)
    
    for number in numbers:
        countable = False
        length = len(number)
        index =  re.search("\D(" + number + ")\D", line).start(1)

        if (lineindex > 0):
            min = index - 1
            max = index + length + 1

            for i in range(min, max):
                if i < len(line) and i >= 0:
                    l = "." + LINES[lineindex-1] + "."
                    c = l[i]
                    if c in SPECCHARS:
                        countable = True

        if index-1 > 0:
            if line[index-1] in SPECCHARS:
                countable = True

        
        if index+length < len(line):
            if line[index+length] in SPECCHARS:
                countable = True

        if (lineindex < len(LINES) - 1):
            min = index - 1
            max = index + length + 1

            for i in range(min, max):
                if i < len(line) and i >= 0:
                    l = "." + LINES[lineindex+1] + "."
                    c = l[i]
                    if c in SPECCHARS:
                        countable = True

        if countable:
            sum += int(number)

        print(number, index, countable)


print("Sum:", sum)
f.close()
# nf.close()