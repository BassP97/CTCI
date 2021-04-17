"""
reverse linked list
"""

def revLL(head):
    curr = head
    prev = None
    while(curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    #note that at the end, prev will be equal to the new head and curr will be equal to Null
    return prev
