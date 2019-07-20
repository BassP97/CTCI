"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes
of the first two lists.
"""

def mergeWrapper(currNode1,currNode2):
    returnHead = new node
    return merge(currNode1,currNode2,returnHead)

def merge(currNode1,currNode2,currStorageNode):
    if currNode1 == Null and currNode2 == Null:
        return Null
    if currNode1.value>currNode2.value or currNode1 == Null:
        currStorageNode.value = node2.value
        currNode2 = currNode2.next
    else:
        currStorageNode.value = node1.value
        currNode1 = currNode1.next
    nextStorageNode = new Node
    currStorageNode.next = merge(currNode1,currNode2,nextStorageNode)
    return currStorageNode
