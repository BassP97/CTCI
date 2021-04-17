"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

def main(currNode):
    if (currNode == null):
        return
    temp = currNode.left.value
    currNode.left.value = currNode.right.value
    currNode.right.value = temp
    main(currNode.left)
    main(currNode.right)
    return currNode
