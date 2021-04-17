"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

#searches for an edge and, if one is found, returns a list of all Os to skip in the future
#if an edge isnt found, it flips all the Os in the current "block" to Xs
def searchForEdge(startLoc, board):
    currLoc = startLoc
    foundEdge = False
    stack = [startLoc]
    locationRecorder = []
    while True:
        if len(stack)!=0:
            nextLoc = stack.pop()
            locationRecorder.append(nextLoc)
            if nextLoc[0]+1>=len(board[0]) or nextLoc[0]-1<=len(board[0]) or nextLoc[1]+1>=len(board) or nextLoc[1]-2<=len(board):
                foundEdge = True
                return locationRecorder
            if board[nextLoc[0]+1][nextLoc[1]] == "0":
                stack.append((nextLoc[0]+1,nextLoc[1]))
            if board[nextLoc[0]][nextLoc[1]+1] == "0":
                stack.append((nextLoc[0],nextLoc[1]+1))
            if board[nextLoc[0]-1][nextLoc[1]] == "0":
                stack.append((nextLoc[0]-1,nextLoc[1]))
            if board[nextLoc[0]][nextLoc[1]-1] == "0":
                stack.append((nextLoc[0],nextLoc[1]-1))
        else:
            break
    for locs in locationRecorder:
        board[locs[0]][locs[1]] = "X"
    return []

def surroundedRegions(board):
    coordinateList = []
    toSkip = Set()
    for x in range(0,len(board)):
        for y in range(0,len(board[x])):
            if board[x][y] == "O" and (x,y) not in toSkip:
                skipLater = searchForEdge((x,y), board)
                if skipLater!=[]:
                    for i in skipLater:
                        toSkip.add(i)
    return board

print(surroundedRegions[])
