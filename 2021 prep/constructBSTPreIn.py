"""
Given preorder and inorder traversal of a tree, 
construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

pre-order: root, left, right
inorder: left, root, right
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeTraversal(root):
    if not root:
        return
    treeTraversal(root.left)
    print(root.val)
    treeTraversal(root.right)


def bstPreIn(preorder, inorder):
    print(preorder, inorder, "shit ass")
    if preorder == []:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])
    rootVal = preorder[0]
    inOrderLeftHalf = inorder[:inorder.index(rootVal)]
    leftHalfSet = set(inOrderLeftHalf)
    inOrderRightHalf = inorder[inorder.index(rootVal)+1:]
    borderIndex = 1
    preorderLeftHalf = []
    while borderIndex < len(preorder) and preorder[borderIndex] in leftHalfSet:
        preorderLeftHalf.append(preorder[borderIndex])
        borderIndex += 1
    preorderRightHalf = preorder[borderIndex:]
    return TreeNode(rootVal, bstPreIn(preorderLeftHalf, inOrderLeftHalf), bstPreIn(preorderRightHalf, inOrderRightHalf))


print(treeTraversal(bstPreIn([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
