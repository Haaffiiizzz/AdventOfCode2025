with open("Day2Input.txt", "r") as file:
    ranges = file.read().strip().split(",")
total = 0
for Range in ranges:
    first = int(Range.split("-")[0])
    second = int(Range.split("-")[1])

    for i in range(first, second + 1):
        intStr = str(i)
        n = len(intStr)
        part = intStr[:(n//2) + 1]

        for j in range(n//2 + 1):
            move = False
            for k in range(j+1, n//2 + 1):
                curr = intStr[j:k]
                if len(curr) * intStr.count(curr) == n:
                    total += i
                    move = True
                    break
            if move:
                break    
print(total)