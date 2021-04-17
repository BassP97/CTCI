"""
Write a function to find the 2nd largest element in a binary search tree
"""
def getLargest(node):
    if node.right:
        return getLargest(node.right)
    return node.value

def secondLargestElemBST(node):
    if node.right is None and node.left is None:
        return None
    if node.right is None:
        return getLargest(node.left)
    while node.right is not None:
        parent = node
        node = node.right
    if node.left:
        return getLargest(node.left)
    else:
        return parent.value



