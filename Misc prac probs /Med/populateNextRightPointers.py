"""
You are given a perfect binary tree where all leaves are on the same level, and
every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

"""
#return a tuple with the furthest left and furthest right children of the current level
def retLevelN(n, currNode):
    if n = 1:
        currNode.left.next = currNode.right
        left = currNode.left
        right = currNode.right
        return [left,right]
    retLeft = retLevelN(n-1,currNode.left)
    retRight = retLevelN(n-1,currNode.right)
    retLeft[1].next = retRight[0]
    left = retLeft[0]
    right = retRight[1]
    return [left,right]



def popNextRightPtr(head):
    currLevel = 1
    while True:
        leftAndRightNodes = retLevelN(currLevel, head)
        if leftAndRightNodes == [None,None]:
            break
        currLevel = currLevel+1
    return head
