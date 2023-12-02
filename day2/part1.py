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

    for turn in turns:
        amounts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
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

            amounts[type] = amounts[type] + int(amount)

        if CUBES["red"] < amounts["red"] or CUBES["green"] < amounts["green"] or CUBES["blue"] < amounts["blue"]:
            possible = False

    if possible:
        sum += int(id)

    
    # if CUBES["red"] < amounts["red"] or CUBES["green"] < amounts["green"] or CUBES["blue"] < amounts["blue"]:
    #     print(id, False)
    # else:
    #     sum += int(id)
    #     print(id, True)

print(sum)