"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


"""

def makeGrid(grid):
    retGrid = []
    for i in range(0,len(grid)):
        retGrid.append([])
        for j in range(0,len(grid[i])):
            retGrid[i].append(0)
    retGrid[0][0] = grid[0][0]
    return retGrid


def minPathSum(grid):
    resultGrid = makeGrid(grid)
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if i>0 and j>0:
                resultGrid[i][j] = min(resultGrid[i-1][j], resultGrid[i][j]) + grid[i][j]
            elif i>0:
                resultGrid[i][j] = resultGrid[i-1][j] + grid[i][j]
            elif j>0:
                resultGrid[i][j] = resultGrid[i][j-1] + grid[i][j]
    return resultGrid[len(grid)-1][len(grid[1])-1]
