"""
Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

def sumBst(currNode,min,max):
    if currNode.val<min or currNode.val>max:
        return 0
    else:
        return sumBst(currNode.left)+sumBst(currNode.right)+currNode.value
