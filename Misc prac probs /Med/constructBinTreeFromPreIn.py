"""
Given preorder and inorder traversal of a tree, construct the binary tree.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
Note: You may assume that duplicates do not exist in the tree.
For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

"""
notes -
    first element of preorder is always the root
    first element of inorder is always furthest left

    if we slice inorder at the root then we end up with the left and right subtrees
    [3]
    / \
  [9] [15,20,7]

  We now know that 9 is the end of the left subtree
  Then looking at the next element after 9 in the preorder array, we get the root of the
  right subtree. If we split inorder on that root, we get its left and right subtrees

  Can we do this recursively?
    Each recursive step should determine the current node's value, as well as
    which elements make up the current node's left and right subtrees

    Base case is when the left and right subtrees have 0(or 1?) items to add
"""
def constructBST(preOrder, inOrder):
    if len(inOrder == 1):
        #pretend that this creates a BST node
        return Node(inOrder[0])
    else:
        #get left and right subtrees
        leftSubTree = inOrder[0:inOrder.index(preOrder[0])]
        rightSubTree = inOrder[inOrder.index(preOrder[0])+1:]
        currNode = Node(preOrder[0])

        currItem = preOrder[1]
        leftPreIn = []
        currLoc = 1
        rightSubSet = Set()
        for i in rightSubtree:
            rightSubSet = rightSubSet.append(i)
        while currItem not in rightSubSet:
            leftPreIn = leftPreIn.append(currItem)
            currLoc = currLoc+1
            currItem = preOrder[currLoc]
        currNode.left = constructBST(leftPreIn, leftSubTree)
        currNode.right = constructBST(rightPreIn, rightSubTree)
        return currNode
