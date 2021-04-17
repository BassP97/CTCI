"""
Given preorder and inorder traversal of a tree, construct the binary tree.

note - too lazy to make a tree, pseudo code will have to do
"""
preOrder = []
inOrder = []
preOrLoc = 0
def main(inOrArr, currNode):
    if inOrArr.size()==0:
        return
    else:
        currNode.value = preOrder[preOrLoc]
        preOrLoc = preOrLoc+1
        indexOfNode = inOrArr.find(preOrder[preOrLoc])
        main(inOrArr[:indexOfNode-1], currNode.left)
        main(inOrArr[indexOfNode+1:], currNode.right)
        return
