"""
Given two non-empty binary trees s and t, check whether tree t has exactly 
the same structure and node values with a subtree of s. A subtree of s is 
a tree consists of a node in s and all of this node's descendants. The 
tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s. 
"""
def preOrder(node):
    if node is None:
        return []
    return preOrder(node.left)+preOrder(node.right)+[node.value]

def inOrderList(node):
    if node is None:
        return []
    return inOrderList(node.left)+[node.value]+inOrderList(node.right)

#two binary trees are the same iff their preorder/post order and inorder are the same
def subtreeOfAnotherTree(s,t):
    sTreeIn = inOrderList(s)
    sTreePre = preOrder(s)
    tTreeIn = inOrderList(t)
    tTreePre = inOrderList(t)
    if tTreeIn in sTreeIn and tTreePre in sTreePre:
        return True
    return False