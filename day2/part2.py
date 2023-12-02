f = open("day2/input.txt")

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

GAMES = f.read().split("\n")

sum = 0

for game in GAMES:
    id = game.split(":")[0].split(" ")[1]
    turns = game.split(": ")[1].split("; ")
    possible = True

    amounts = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for turn in turns:
        cubes = turn.split(", ")

        for cube in cubes:
            type = ""
            amount = 0

            if (cube.find("red") > -1):
                amount = cube.split(" red")[0]
                type = "red"
            elif (cube.find("green") > -1):
                amount = cube.split(" green")[0]
                type = "green"
            elif (cube.find("blue") > -1):
                amount = cube.split(" blue")[0]
                type = "blue"

            if int(amount) > amounts[type]:
                amounts[type] = int(amount)

    print(id, amounts)
    sum += int(amounts["red"]) * int(amounts["green"]) * int(amounts["blue"])


print(sum)