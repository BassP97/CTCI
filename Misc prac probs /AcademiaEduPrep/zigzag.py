"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

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

#simple level order traversal queue method using a flag for left to right or right to left
def queueMethod(head):
    queue = deque()
    queue.appendleft(head)
    rightOrder = True
    solArr = []
    currLevelArr = [head.value]
    while queue:
        solArr.append(currLevelArr)
        currLevelArr = []
        nextLevelQueue = deque()
        while queue:
            currNode = queue.pop()
            currLevelArr.append(currNode.value)
            if rightOrder:
                if currNode.right():
                    nextLevelQueue.appendleft(currNode.right)
                if currNode.left():
                    nextLevelQueue.appendleft(currNode.left)
            else:
                if currNode.left():
                    nextLevelQueue.appendleft(currNode.left)
                if currNode.right():
                    nextLevelQueue.appendleft(currNode.right)
        rightOrder = not rightOrder
        queue = nextLevelQueue
        
#Alternative method that just reverses each level
def revMethod(head):
    queue = deque(head)
    right = True
    res = []
    while queue:
        nextLevelQueue = deque()
        currLevel = []
        queueLen = len(queue)
        for i in range(queueLen):
            item = queue.pop()
            currLevel.append(item.value)
            if item.left:
                nextLevelQueue.append(item.left)
            if item.right:
                nextLevelQueue.append(item.right)
        if not right:
            nextLevelQueue.reverse()
        res.append(currLevel)