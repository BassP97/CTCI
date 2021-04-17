"""
You are given a perfect binary tree where all
leaves are on the same level, and every parent
has two children. The binary tree has the following
definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
"""


def binNextPtr(root):
    if not root:
        return
    if not root.left:
        return root
    currLevel = [root]
    levelNum = 0
    while currLevel:
        prevNode = currLevel[0]
        nextLevel = []
        if prevNode.left:
            nextLevel.append(prevNode.left)
            nextLevel.append(prevNode.right)
        for node in currLevel[1:]:
            prevNode.next = node
            prevNode = node
            if prevNode.left:
                nextLevel.append(node.left)
                nextLevel.append(node.right)
        currLevel[-1].next = None
        currLevel = nextLevel
    return root
