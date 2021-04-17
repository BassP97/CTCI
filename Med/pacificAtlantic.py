"""
Given an m x n matrix of non-negative integers representing the height of each
unit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to
another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.

"""
import copy


def pacificAtlantic(grid):
    retArr = []
    seen = [[]]
    for i in grid:
        for j in i:
            seen[i][j] == False
    for i in range(0,len(grid)):
        for j in range(0,len(i)):
            pacific = False
            atlantic = False
            seenTemp = copy.deepcopy(seen)
            stack = deque()
            stack.appendleft((i,j))
            seenTemp[i][j] = True
            while len(stack)!=0:
                currLoc = stack.pop()
                if currLoc[0]==0 or currLoc[1]==0:
                    pacific = True
                if currLoc[0]==len(grid)-1 or currLoc[1] == len(grid[i])-1:
                    atlantic = True
                if pacific and atlantic:
                    retArr.append((currLoc[0],currLoc[1]))
                    break
                else:
                    currVal = grid[currLoc[0]][currLoc[1]]
                    if currLoc[0]!=0 and grid[currLoc[0]-1][currLoc[1]] <= currVal and not seenTemp[currLoc[0]-1][currLoc[1]]:
                        stack.appendleft((currLoc[0]-1,currLoc[1]))
                        seenTemp[currLoc[0]-1][currLoc[1]] = True
                    if currLoc[1]!=0 and grid[currLoc[0]][currLoc[1]-1] <= currVal and not seenTemp[currLoc[0]][currLoc[1]-1]:
                        stack.appendleft((currLoc[0],currLoc[1]-1))
                        seenTemp[currLoc[0]][currLoc[1]-1] = True
                    if currLoc[0]!=len(grid)-1 and grid[currLoc[0]+1][currLoc[1]] <= currVal and not seenTemp[currLoc[0]+1][currLoc[1]]:
                        stack.appendleft((currLoc[0],currLoc[1]-1))
                        seenTemp[currLoc[0]+1][currLoc[1]] = True
                    if currLoc[0]!=len(grid[i])-1 and grid[currLoc[0]][currLoc[1]+1] <= currVal and not seenTemp[currLoc[0]][currLoc[1]+1]:
                        stack.appendleft((currLoc[0],currLoc[1]-1))
                        seenTemp[currLoc[0]][currLoc[1]+1] = True
    return retArr

#better way - add all atlantic/pacific ocean tiles to a queue, add cells visited by BOTH to the grid
#we're going to return
