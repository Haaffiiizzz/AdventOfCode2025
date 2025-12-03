with open("Day3Input.txt", "r") as file:
    lines = file.readlines()

total = 0
for line in lines:
    lineList = list(line.strip())
    newList = []
    for i, j in enumerate(lineList):
        newList.append((j, i))
    res = ""
    currentMaxIndex = -1
    n = len(lineList)
    for i in range(12, 0, -1):
        currentMax, currentMaxIndex = max(newList[currentMaxIndex+1:n-i+1], key= lambda x: x[0])
        res += currentMax
    total += int(res)

print(total)