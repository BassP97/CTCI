""""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use
an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1,
then there is no cycle in the linked list.

Return true if there is a cycle, false otherwise

I am very lazy and don't wanna implement a linked list, so
the pure logic will have to do
"""

def detectCycle(head):
    slowPtr = head
    fastPtr = head.next
    while(slowPtr != fastPtr):
        if (fastPtr == null or fastPtr.next == null):
            return False
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next
    return True
