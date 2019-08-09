"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Recursive solution is trivial, could you do it iteratively?
"""

def bstOrderIterative(head):
    nodeStack = [head.val]
    while (len(nodeStack)!=0):
        if nodeStack.top.left != null:
            nodeStack.append(nodeStack.top.left)
        curr = nodeStack.pop
        print curr
        if curr.right!=null:
            nodeStack.append(curr.right)
