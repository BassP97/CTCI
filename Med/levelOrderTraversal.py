"""
Given a binary tree, return the level order traversal of its 
nodes' values. (ie, from left to right, level by level).
"""
def getMaxDepth(root):
    if root == None:
        return 0
    return max(getMaxDepth(root.left), getMaxDepth(root.right))+1

def levelOrderInternal(root, dipLen):
    if root is None:
        return []
    if dipLen == 0:
        return root.value()
    return levelOrderInternal(root.left,dipLen-1)+levelOrderInternal(root.right,dipLen-1)
    
def levelOrderTraversal(root):
    maxDepth = getMaxDepth(root)
    retArr = []
    for i in range(maxDepth):
        retArr.append(levelOrderInternal(root,i))

def levelOrderQueue(root):
    queue = [root]
    while len(queue) > 0:
        currNode = queue.pop()
        print(currNode)
        if currNode.left:
            queue.insert(0,currNode.left)
        if currNode.right:
            queue.insert(0,currNode.right)
        
    