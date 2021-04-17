"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?
"""
itemToSwap = None

def recoverBst(currNode, max, min):
    checkLeft = True
    checkRight = True
    if currNode.left == None:
        checkLeft = False
    if currNode.right == None:
        checkRight = False
    if checkLeft and currNode.left.value>min:
        if itemToSwap != None:
            temp = currNode.left.value
            currNode.left.value = itemToSwap.value
            itemToSwap.value = temp
        else:
            itemToSwap = currNode
    if checkLeft and currNode.left.value<max:
        if itemToSwap != None:
            temp = currNode.left.value
            currNode.left.value = itemToSwap.value
            itemToSwap.value = temp
        else:
            itemToSwap = currNode
    recoverBst(currItem.left,currItem.value,min)
    recoverBst(currItem.right,max,currItem.value)
    return
