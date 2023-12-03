#tried:
#74224027 low
#75805607 answer

import os
import re
from textwrap import wrap

f = open("day3/input.txt")

SPECCHARS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "/", "|", "\\"]
LINES = f.read().split("\n")
MATRIX = []

sum = 0

for lineindex, line in enumerate(LINES):
    if line.find("*") > -1:
        index = 0
        for asterisk in re.findall("(\*)", line):
            index = line.index("*", index+1)
            numbers = {
                "left": "",
                "right": "",
                "top": "",
                "topleft": "",
                "topright": "",
                "bottom": "",
                "bottomleft": "",
                "bottomright": "",
            }

            if index > 0:
                i = 1
                while line[index-i].isdigit():
                    numbers["left"] += line[index-i]
                    i += 1
                
                numbers["left"] = numbers["left"][::-1]

            if index < len(line):
                i = 1
                while index + i < len(line) and line[index+i].isdigit():
                    numbers["right"] += line[index+i]
                    i += 1
            
            if lineindex > 0:
                if LINES[lineindex-1][index].isdigit() or LINES[lineindex-1][index-1].isdigit() or LINES[lineindex-1][index+1].isdigit():
                    if LINES[lineindex-1][index].isdigit():
                        numbers["top"] = LINES[lineindex-1][index]

                        i = 1
                        while index + i < len(line) and LINES[lineindex-1][index-i].isdigit():
                            numbers["top"] += LINES[lineindex-1][index-i]
                            i += 1
                        
                        numbers["top"] = numbers["top"][::-1]

                        i = 1
                        while index + i < len(line) and LINES[lineindex-1][index+i].isdigit():
                            numbers["top"] += LINES[lineindex-1][index+i]
                            i += 1
                    else:
                        if LINES[lineindex-1][index-1].isdigit():
                            i = 1
                            while index + i < len(line) and LINES[lineindex-1][index-i].isdigit():
                                numbers["topleft"] += LINES[lineindex-1][index-i]
                                i += 1
                        
                            numbers["topleft"] = numbers["topleft"][::-1]

                        if LINES[lineindex-1][index+1].isdigit():
                            i = 1
                            while index + i < len(line) and LINES[lineindex-1][index+i].isdigit():
                                numbers["topright"] += LINES[lineindex-1][index+i]
                                i += 1


            if lineindex < len(LINES)-1:
                if LINES[lineindex+1][index].isdigit() or LINES[lineindex+1][index-1].isdigit() or LINES[lineindex+1][index+1].isdigit():
                    if LINES[lineindex+1][index].isdigit():
                        numbers["bottom"] = LINES[lineindex+1][index]

                        i = 1
                        while index + i < len(line) and LINES[lineindex+1][index-i].isdigit():
                            numbers["bottom"] += LINES[lineindex+1][index-i]
                            i += 1
                        
                        numbers["bottom"] = numbers["bottom"][::-1]

                        i = 1
                        while index + i < len(line) and LINES[lineindex+1][index+i].isdigit():
                            numbers["bottom"] += LINES[lineindex+1][index+i]
                            i += 1
                    else:
                        if LINES[lineindex+1][index-1].isdigit():
                            i = 1
                            while index + i < len(line) and LINES[lineindex+1][index-i].isdigit():
                                numbers["bottomleft"] += LINES[lineindex+1][index-i]
                                i += 1
                        
                            numbers["bottomleft"] = numbers["bottomleft"][::-1]

                        if LINES[lineindex+1][index+1].isdigit():
                            i = 1
                            while index + i < len(line) and LINES[lineindex+1][index+i].isdigit():
                                numbers["bottomright"] += LINES[lineindex+1][index+i]
                                i += 1


            multiply = []
            print(lineindex+1, numbers)

            for key, number in numbers.items():
                if (number.isdigit()):
                    multiply.append(int(number))
                

            if len(multiply) == 2:
                sum += multiply[0] * multiply[1]

print("Sum:", sum)
f.close()
# nf.close()