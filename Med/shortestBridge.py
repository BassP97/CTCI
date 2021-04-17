"""
934. Shortest Bridge
Medium

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally 
connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer 
is at least 1.)
"""

"""
Strategy: 
    1. find each island and flip one to a different symbol
    2. use Dijkstra's to find shortest path from island 1 to 2
    3. Return num nodes
"""
import copy

def markIslandOne(islands, start):
    x = start[0]
    y = start[1]
    while True:
        if x+1>len(islands[start[0]])
        

def flippedIslands(islands):
    tempIslands = copy.deepcopy(islands)
    foundOne = True
    for i in range(0,len(islands)):
        for j in range(0,len(islands[i])):
            if islands[i][j] == 1 and foundOne == False:
                markIslandOne(tempIslands, (i,j))

def shortestBridge(islands):
    flippedIslands = flipIslands(islands)
    return dijkstra(flippedIslands)


assert(shortestBridge([[0,1],[1,0]]) == 1)
assert(shortestBridge([[0,1,0],[0,0,0],[0,0,1]]) == 2)
assert(shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]) == 1) 