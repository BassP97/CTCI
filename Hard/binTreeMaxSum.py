"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path
must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
currMax = 0
def binTreeMaxSum(root):
    binTreeMaxSumInternal(root)
    return currMax

def binTreeMaxSumInternal(root):
    if root == Null:
        return 0
    binTreeLeft = max(0, binTreeMaxSumInternal(root.left))
    binTreeRight = max(0, binTreeMaxSumInternal(root.right))
    withRoot = max(binTreeLeft,binTreeRight)+root.value
    if withRoot>currMax:
        currMax = withRoot
    return withRoot
