#tried:
#54581 answer

f = open("day1/input.txt")
INPUT = f.readlines()
NUMBERS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

TXTNUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

total = 0

for i in INPUT:
    print(i.split("\n")[0])

    firstindex = len(i)
    firstnumber = 0
    lastindex = 0
    lastnumber = 0

    for a in NUMBERS:
        if (i.find(a) > -1):
            if i.find(a) < firstindex:
                firstindex = i.find(a)
                firstnumber = a
            
            if i.rfind(a) > lastindex:
                lastindex = i.rfind(a)
                lastnumber = a

    print(firstnumber, lastnumber)

    try:
        firstnumber = int(firstnumber)
    except:
        firstnumber = TXTNUMBERS.index(firstnumber)

    try:
        lastnumber = int(lastnumber)
    except:
        lastnumber = TXTNUMBERS.index(lastnumber)

    if lastnumber == 0:
        lastnumber = firstnumber

    print(int(str(firstnumber) + str(lastnumber)))

    total += int(str(firstnumber) + str(lastnumber))

print("Total: ", total)