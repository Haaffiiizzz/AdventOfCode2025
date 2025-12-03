with open("Day3Input.txt", "r") as file:
    lines = file.readlines()

total = 0
for line in lines:
    lineList = list(line.strip())
    newList = sorted(lineList, reverse=True)

    firstMax = newList[0]
    if lineList.index(firstMax) == len(lineList) -1:
        firstMax = newList[1]

    secondMax = max(lineList[lineList.index(firstMax) + 1:])
    res = firstMax + secondMax
    total += int(res)

print(total)