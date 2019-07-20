"""
Given a linked list, remove the n-th node from the end of list

Too lazy to write a real linked list so this will have to do
"""

#note - doesn't work for head or tail removal
def removeNthFromEnd(currNode,n):
    if currNode.next == Null
        return 1
    else:
        itemNumFromEnd = removeNthFromEnd(currNode.next,n)+1
        if itemNum == n+1:
            temp = currNode.next
            currNode.next = temp.next
            delete temp
            return itemFromEnd+1
