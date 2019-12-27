"""
Write a function to see if a binary tree is superbalanced
(a new tree property we just made up).

A tree is "superbalanced" if the difference between the 
depths of any two leaf nodes is no greater than one.
"""
def superBalancedInternal(node):
    if node == None:
        return [0,0]
    loHiLeft = superBalanced(node.left)
    loHiRight = superBalanced(node.right)
    loLeft, hiLeft = loHiLeft[0],loHiLeft[1]
    loRight, hiRight = loHiRight[0],loHiRight[1]

    lo = min(loLeft, loRight)+1
    hi = min(hiLeft, hiRight)+1
    return [lo,hi]

def superBalanced(node):
    loHi = superBalancedInternal(node)
    if loHi[1]-loHi[0] > 1:
        return False
    return True