"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

def LLIntersect(headA, headB):
    ptr1 = headA
    prt1A = True
    ptr2 = headB
    ptr2A = False
    endA = None
    endB = None
    while True:
        if endA is not None and endB is not None:
            if endA != endB:
                return False
        if ptr1 == ptr2:
            return True
        if ptr1.next is None:
            if ptr1A:
                endA = ptr1
                ptr1 = headB
                ptr1A = False
            else:
                ptr1 = headA
                ptr1A = True 
        else:
            ptr1 = ptr1.next
        if ptr2.next is None:
            if ptr2A:
                endA = ptr2
                ptr2 = headB
                ptr2A = False
            else:
                ptr2 = headA
                ptr2A = True 
        else:
            ptr2 = ptr2.next
    

            
            
