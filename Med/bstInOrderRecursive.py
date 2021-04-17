"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
"""
def getLevel(node, level):
    if node == null:
        return []
    if level == 0:
        return [node.value]
    else:
        return getLevel(node.left,level-1)+getLevel(node.right,level-1)

#n^2 time complexity for a fully unbalanced tree, for a perfectly balanced tree n log(n)
def inOrder(root):
    levelOrder = []
    while True:
        currLevel = getLevel(root,i)
        if currLevel = []:
            break
        else:
            levelOrder.append(currLevel)
    return levelOrder
