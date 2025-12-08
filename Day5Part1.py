with open("Day5Input.txt", "r") as file:
    lines = file.readlines()
numDict = []
count = 0
j = 0
for line in lines:
    print(j)
    j+= 1
    if line.strip():
        if "-" in line:
            start = int(line.strip().split("-")[0])
            end = int(line.strip().split("-")[1])

            numDict.append((start, end))

        else:
            num = int(line.strip())
            for i in numDict:
                if num >= i[0] and num <= i[1]:
                    count += 1
                    break
print(count)
            
