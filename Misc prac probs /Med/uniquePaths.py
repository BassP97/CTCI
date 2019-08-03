"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram
below).

How many possible unique paths are there?
"""

def addNeighborsToSelf(row,column,grid):
    sum = grid[row][column]
    if row>0:
        sum = sum+grid[row-1][column]
    if column>0:
        sum = sum+grid[row][column-1]
    return sum

def printGrid(grid):
    for i in grid:
        print i
    print ""

def findNumPaths(m,n):
    grid = []
    for i in range(0,n):
        grid.append([0]*m)
    grid[0][0] = 1
    for row in range(0,len(grid)):
        for column in range(0,len(grid[row])):
            grid[row][column] = addNeighborsToSelf(row,column,grid)
    return grid[len(grid)-1][len(grid[0])-1]


assert(findNumPaths(7,3) == 28)
assert(findNumPaths(3,2) == 3)
