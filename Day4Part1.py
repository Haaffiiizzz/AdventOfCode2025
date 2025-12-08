grid = []

with open("Day4Input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        grid.append(list(line.strip()))

n, m = len(grid), len(grid[0])
res = 0



for i in range(n):
    for j in range(m):
        curr = grid[i][j]
        count = 0

        if curr == "@":
            
            if j > 0: # we can go left
                if grid[i][j-1] == "@": # left
                    count += 1
                
                if i > 0: # we can go up left
                    if grid[i-1][j-1] == "@":
                        count += 1

                if i < n -1: # we can do down left
                    if grid[i+1][j-1] == "@":
                        count += 1

            if j < m - 1: # we can go right
                if grid[i][j+1] == "@": #right
                    count += 1
                
                if i > 0: #up right
                    if grid[i-1][j+1] == "@":
                        count += 1

                if i < n - 1: #down right
                    if grid[i+1][j+1] == "@":
                        count += 1
            
            if i > 0: #up
                if grid[i-1][j] == "@":
                    count += 1
            
            if i < n - 1: #down
                if grid[i + 1][j] == "@":
                    count  += 1 
        else:
            count = 8

        if count < 4:
            res += 1
   

print(res)

                



            
