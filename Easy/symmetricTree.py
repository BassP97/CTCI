"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).
"""

def traverseArr(root):
    if root==None:
        return [None]
    return traverseArr(root.left)+[root.value]+traverseArr(root.right)

def symmTree(root)
    return traverseArr(root.left) == traverseArr(root.right)
