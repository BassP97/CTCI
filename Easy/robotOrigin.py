"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a
sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents
its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the
robot returns to the origin after it finishes all of its moves, return true.
Otherwise, return false.
"""

def robotOrigin(moves):
    moveStack = []
    moveDict = {}
    for move in moves:
        if move in moveDict.keys():
            moveDict[move] = moveDict[move]+1
        else:
            moveDict[move] = 1
    return moveDict["U"] == moveDict["D"] and moveDict["L"] == moveDict["R"]

assert(robotOrigin("UUDLLRDR") == True)
assert(robotOrigin("UUDLRDR") == False)
