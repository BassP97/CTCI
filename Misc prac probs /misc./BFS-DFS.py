"""
Implement breadth first search in python using an adjacency dictionary matrix
and a list of nodes
"""
from collections import deque

class node:
    def __init__(self):
        self.value = 0
        self.parent = None
    def setParent(self, parent):
        self.parent = parent

def bfs(nodes, adjDict, startNode, toFind):
    seenQueue = deque()
    seen = {}
    for node in nodes:
        seen[node] = False
    seenQueue.appendleft(startNode)
    seen[startNode] = True
    while len(seenQueue) != 0:
        currNode = seenQueue.pop()
        if v = toFind:
            return v
        else:
            for node in adjDict[v]:
                if not seen[node]:
                    seenQueue.appendleft(node)
                    node.setParent(v)
                    seen[node] = True

def dfs(nodes, adjDict, startNode, toFind):
