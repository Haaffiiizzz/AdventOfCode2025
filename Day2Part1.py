with open("Day2Input.txt", "r") as file:
    ranges = file.read().strip().split(",")
total = 0
for Range in ranges:
    first = int(Range.split("-")[0])
    second = int(Range.split("-")[1])

    for i in range(first, second + 1):
        intStr = str(i)
        if len(intStr)% 2 == 0:
            n = len(intStr)
            if intStr[:n//2] == intStr[n//2:]:
                total += i
print(total)

