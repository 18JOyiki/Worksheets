# is a given list of lists of integers that represent a 2
# dimensional grid with n rows and m columns. A cell is called a
# dominant cell if it has a strictly greater value than all of its
# neighbors. Two cells are neighbors when they share a common
# side or a common corner, so a cell can have up to 8 neighbors.
# Find the number of dominant cells in the grid.
#
# Function Description
# Complete the function numCells in the editor below.
#
# numCells has the following parameter(s):
#
# int grid[n][m]: a 2-dimensional array of integers
#
# Returns
#
# int: the number of dominant cells in the grid

grid = [
    [1,2,7],
    [4, 5, 6],
    [8, 8, 9],
    [2, 4, 6],
    [4, 6, 3],
    [9, 3, 6],
    [4, 6 ,7],
    [ 8, 6, 8],
]
def numCells(grid):
    dominant = 0
    dominants = []
    for n in range(len(grid)):
        for m in range(len(grid[n])):
            if n == 0:
                if m == 0:
                    if grid[n][m] > grid[n + 1][m] and grid[n][m] > grid[n][m + 1] and grid[n][m] > grid[n + 1][m + 1]:
                        dominant += 1
                        dominants.append((n, m))
                elif m == len(grid[n]) - 1:
                    if grid[n][m] > grid[n + 1][m] and grid[n][m] > grid[n][m - 1] and grid[n][m] > grid[n + 1][m - 1]:
                        dominant += 1
                        dominants.append((n, m))
                else:
                    if grid[n][m] > grid[n][m + 1] and grid[n][m] > grid[n][m - 1] and grid[n][m] > grid[n + 1][m + 1]\
                            and grid[n][m] > grid[n + 1][m] and grid[n][m] > grid[n + 1][m - 1]:
                        dominant += 1
                        dominants.append((n, m))
            elif n == len(grid) - 1:
                if m == 0:
                    if grid[n][m] > grid[n - 1][m] and grid[n][m] > grid[n][m + 1] and grid[n][m] > grid[n - 1][m + 1]:
                        dominant += 1
                        dominants.append((n, m))
                elif m == len(grid[n]) - 1:
                    if grid[n][m] > grid[n - 1][m] and grid[n][m] > grid[n][m - 1] and grid[n][m] > grid[n - 1][m - 1]:
                        dominant += 1
                        dominants.append((n, m))
                else:
                    if grid[n][m] > grid[n][m + 1] and grid[n][m] > grid[n][m - 1] and grid[n][m] > grid[n - 1][m + 1]\
                            and grid[n][m] > grid[n - 1][m] and grid[n][m] > grid[n - 1][m - 1]:
                        dominant += 1
                        dominants.append((n, m))
            else:
                if m == 0:
                    if grid[n][m] > grid[n][m + 1] and grid[n][m] > grid[n - 1][m] and grid[n][m] > grid[n + 1][m] and\
                    grid[n][m] > grid[n - 1][m + 1] and grid[n][m] > grid[n + 1][m + 1]:
                        dominant += 1
                        dominants.append((n, m))
                elif m == len(grid[n]) - 1:
                    if grid[n][m] > grid[n][m - 1] and grid[n][m] > grid[n - 1][m] and grid[n][m] > grid[n + 1][m] and\
                    grid[n][m] > grid[n - 1][m - 1] and grid[n][m] > grid[n + 1][m - 1]:
                            dominant += 1
                            dominants.append((n, m))
                else:
                    if grid[n][m] > grid[n + 1][m] and grid[n][m] > grid[n - 1][m] and grid[n][m] > grid[n][m + 1] and\
                    grid[n][m] > grid[n][m - 1] and grid[n][m] > grid[n - 1][m - 1] and \
                    grid[n][m] > grid[n + 1][m + 1] and grid[n][m] > grid[n + 1][m - 1] and grid[n][m] >\
                    grid[n - 1][m + 1]:
                        dominant += 1
                        dominants.append((n, m))

    print dominants
    return dominant
print(numCells(grid))