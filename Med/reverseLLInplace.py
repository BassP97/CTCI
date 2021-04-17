"""
Write a function for reversing a linked list. Do it in place.

Your function will have one input: the head of the list.

Your function should return the new head of the list.

Here's a sample linked list node class: 
"""

def revLL(head):
    if head.next is None:
        return head
    curr = head.next
    prev = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
        