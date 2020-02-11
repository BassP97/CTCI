"""
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory 
buffer, or transmitted across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is 
no restriction on how your serialization/deserialization algorithm should 
work. You just need to ensure that a binary tree can be serialized to a 
string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""
def getDepth(root):
    if root is None:
        return 0
    return max(getDepth(root.left), getDepth(root.right))+1

def levelOrder(root,depth):
    if depth == 0:
        if root.value is None:
            return['none']
        return [root.value]
    return levelOrder(root.left,depth-1)+levelOrder(root.right, depth-1)

def serializeBST(root):
    depth = getDepth(root)
    retArr = []
    for i in range(depth):
        retArr = retArr + levelOrder
