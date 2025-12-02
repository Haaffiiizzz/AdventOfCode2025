with open("Day1Input.txt", "r") as file:
    lines = file.readlines()
code = 50
count = 0
# for line in lines:
#     num = int(line.strip()[1:]) 
#     move = line[0]
#     if move == "R":
#         code = (code + num) % 100
#     else:
#         code = (code - num) % 100
    
#     if code == 0:
#         count += 1


for line in lines:
    og = int(line.strip()[1:]) 
    num = int(line.strip()[1:]) 
    move = line[0]


        
    if move == "R":
        rem = 100 - code
    else:
        rem = code
    if rem == 0:
        rem = 100
    if num >= rem:
        count += 1
        num -= rem
    while num >= 100:
        count += 1
        num -= 100
    if move == "R":
        code = (code + og) % 100
    else:
        code = (code - og) % 100
print(count)