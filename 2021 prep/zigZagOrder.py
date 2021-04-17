"""
Given a binary tree, return the zigzag level order traversal
of its nodes' values. (ie, from left to right, then right to
left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

"""
from collections import deque


def zigZag(root):
    if not root:
        return [[]]
    currLevel = deque(root)
    nextLevel = deque()
    zig = True
    levels = []
    while(currLevel):
        currLevelContents = []
        for node in currLevel:
            currLevelContents.append(node.value)
            if zig:
                if node.left:
                    nextLevel.appendleft(node.left)
                if node.right:
                    nextLevel.appendleft(node.right)
            else:
                if node.right:
                    nextLevel.appendleft(node.right)
                if node.left:
                    nextLevel.appendleft(node.left)
        zig = not zig
        currLevel = nextLevel
        nextLevel = deque()
        levels.append(currLevelContents)
    return levels
