def dictSol(currNode, count):
    if currNode is None:
        return count
    count[currNode.value] = count.get(currNode.value, 0) + 1
    dictSol(currNode.left, count)
    dictSol(currNode.right, count)
    return count

def dictSolWrapper(currNode):
    count = dictSol(currNode, {})
    max_ct = max(count.itervalues())
    return [k for k, v in count.iteritems() if v == max_ct]

def bstMode(currNode):
    if currNode is None:
        return(-1, -1)
    if currNode.left is None and currNode.right is None:
        return (1, [currNode.value])
    else:
        leftMode = bstMode(currNode.left)
        rightMode = bstMode(currNode.right)
        if leftMode[0] == -1:
            if rightMode[1] == currNode.value:
                return (rightMode[0]+1, currNode.value)
        elif leftMode[0] == -1:
            if leftMode[1] == currNode.value:
                return (leftMode[0]+1, currNode.value)
        else:         
            if leftMode[1] == currNode.value:
                leftMode[0]+=1
            if rightMode[1] == currNode.value:
                rightMode[0]+=1
            if leftMode[0]>rightMode[0]:
                return leftMode
            elif leftMode[0]<rightMode[0]:
                return rightMode
            else:
                return (rightMode[0], rightMode[1]+leftMode[1])

def bstModeWrapper(root):
    modeTuple = bstMode(root)
    return [modeTuple[1]]

