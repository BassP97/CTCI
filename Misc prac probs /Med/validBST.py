"""
Write a function to check that a binary tree is a valid binary search tree.
"""

#[low,high,validBit]
def validBST(node):
    right = []
    left = []
    retArr = [-float('inf'),float('inf'),0]
    if node.left is None and node.right is None:
        return [node.value,node.value,1]

    if node.right:
        right = validBST(node.right)
        if right[2] == 0:
            return retArr
        if node.value>right[1]:
            return retArr
        retArr[1] = right[1]

    if node.left:
        left = validBST(node.left)
        if left[2] == 0:
            return retArr
        if node.value<=left[1]:
            return retArr
        left[0] = left[0]

    retArr[2] = 1
    return retArr

def validBSTWrapper(node):
    temp = validBST(node)
    if temp[2] == 1:
        return True
    return False