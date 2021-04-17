"""
You have a linked list and want to find the kth to last node.

Write a function kth_to_last_node() that takes an integer 
k and the head_node of a singly-linked list, and returns 
the kth to last node in the list.

For example: 
"""

def kLastNode(head,k):
    curr = head
    lLen = 0
    while curr is not None:
        lLen = lLen+1
        curr = curr.next
    index = lLen-k
    currLoc = 0
    curr = head
    while currLoc != index:
        currLoc = currLoc+1
        curr = curr.next
    return curr.value

#create two pointers w/ dist k between them. When the front pointer reaches the end of the list,
#return the back pointer's value
def kLastTwoPtr(head,k):
    kDist = head
    for i in range(1,k):
        kDist = kDist.next
    curr = head
    while kDist.next:
        curr = curr.next
        kDist = kDist.next
    return curr.value