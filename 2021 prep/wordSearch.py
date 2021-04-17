"""
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where "adjacent" cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""
from collections import deque


def neighbors(i, j, iDim, jDim):
    res = []
    if i > 0:
        res.append((i-1, j))
    if i < iDim-1:
        res.append((i+1, j))
    if j > 0:
        res.append((i, j-1))
    if j < jDim-1:
        res.append((i, j+1))
    return res


def dfsSearch(word, coords, grid):
    if len(word) == 0 or len(word) == 1:
        return True
    pathsTaken = {}
    stack = deque()
    stack.append(coords)
    nextChrIndex = 1
    while stack:
        currCoord = stack[-1]
        stackSet = set(stack)
        if currCoord not in pathsTaken.keys():
            pathsTaken[currCoord] = []
        nextChr = word[nextChrIndex]
        print("checking coordinate ", currCoord[0], currCoord[1],
              " 's neighbors against char ", nextChr)
        found = False
        print('curr coordinate: ', currCoord)
        print("stack set: ", stackSet)
        print("paths previously taken at curr coordinate ",
              pathsTaken[currCoord])
        for neighbor in neighbors(currCoord[0], currCoord[1], len(grid), len(grid[0])):
            if grid[neighbor[0]][neighbor[1]] == nextChr and (neighbor[0], neighbor[1]) not in pathsTaken[currCoord] and (neighbor[0], neighbor[1]) not in stackSet:
                pathsTaken[currCoord].append((neighbor[0], neighbor[1]))
                found = True
                stack.append((neighbor[0], neighbor[1]))
                nextChrIndex += 1
                break
        if nextChrIndex == len(word):
            return True
        if not found:
            print('none found\n')
            pathsTaken[stack.pop()] = []
            nextChrIndex -= 1
    return False


def exist(board, word):
    print('\nnew run with word', word)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                if dfsSearch(word, (i, j), board):
                    return True
    return False


assert(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]], "ABCCED") == True)
assert(exist([["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]], "ABCB") == False)
assert(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]], "SEE") == True)
assert(exist([["a", "b"], ["c", "d"]], "abcd") == False)
assert(exist([["A", "B", "C", "E"],
              ["S", "F", "E", "S"],
              ["A", "D", "E", "E"]], "ABCESEEEFS") == True)
