"""
For a binary tree T, we can define a flip operation as follows: 
    choose any node
    swap the node's left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and 
only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are 
flip equivalent.  The trees are given by root nodes root1 and root2.
"""

def flipBST(node1, node2):
    if node1 is None and node2 is not None:
        return False
    if node1 is not None and node2 is None:
        return False
    if node1 is None and node2 is None:
        return True
    return (flipBST(node1.left, node2.right) and flipBST(node1.right, node2.left)) or (flipBST(node1.left, node2.left) and flipBST(node1.right, node2.right))
    

    