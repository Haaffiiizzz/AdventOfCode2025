with open("Day5Input.txt", "r") as file:
    lines = file.readlines()
numDict = []

for line in lines:
    start = int(line.strip().split("-")[0])
    end = int(line.strip().split("-")[1])

    numDict.append((start, end))

numDict.sort(key = lambda x: x[0])

total = numDict[0][1]- numDict[0][0] + 1

prev = numDict[0][1]

for start, end in numDict[1:]:
    if end < prev:
        continue
    res = end - max(prev + 1, start) + 1
    total += res
    prev = end

print(total)