def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    initRow = row - row % 3
    initCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + initRow][j + initCol] == num:
                return False
    return True

base = 9

def SudukoSolver(grid, row, col):
 
    if (row == base - 1 and col == base):
        return True
    if col == base:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return SudukoSolver(grid, row, col + 1)
    for num in range(1, base + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if SudukoSolver(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
