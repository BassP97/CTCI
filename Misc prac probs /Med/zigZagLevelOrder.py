"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

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

#crappy way - standard level order followed by reversing
def levelOrder(currNode, level, leftToRight):
    if currNode == None:
        return []
    if level == 0:
        return [currNode.value]
    else:
        if leftToRight == True:
            return levelOrder(currNode.left,level-1,leftToRight) + levelOrder(currNode.right,level-1,leftToRight)
        else:
            return levelOrder(currNode.right,level-1,leftToRight) + levelOrder(currNode.left,level-1,leftToRight)

def zigZag(root)
    currLevel = 0
    currOrientation = True
    retArr = []
    while True:
        currArr = levelOrder(root,currLevel,currOrientation)
        if currArr == []
            break;
        retArr = retArr+currArr
        currOrientation = not currOrientation
        currLevel = currLevel+1
    return retArr
