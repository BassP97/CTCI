"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

The binary tree is stored in an array as follows:

"""

def main(bst):s
    for i in range(0, len(bst)):
        if ((2*i)+1 <= len(bst)-1):
            if((bst[(2*i)+1] is not None) and (bst[(2*i)+1]>bst[i])):
                print("The left child of ", bst[i], " ", bst[(2*i)+1], " is greater than its parent")
                return False
        if ((2*i)+2 <= len(bst)-1):
            if(bst[(2*i)+2] is not None and bst[(2*i)+2]<bst[i]):
                print("The right child of ", bst[i], "-", bst[(2*i)+1], " is greater than its parent")
                return False
    return True

assert(main([2,1,3]) == True)
assert(main([5,1,4,None,None,3,6]) == False)
