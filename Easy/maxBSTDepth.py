"""
I am too lazy to make a BST so pseudo-code will have to do

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
def main(currNode):
    if currNode == null:
        return 0
    return max(main(currNode.left), main(currNode.right))+1
