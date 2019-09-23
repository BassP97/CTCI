"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""
def linkedListPal(head):
    stack = []
    curr = head
    while (curr!=None):
        stack.append(curr.value)
        curr = curr.next
    curr = head
    while (curr!=None):
        temp = stack.pop()
        if temp != curr.value:
            return False
        curr = curr.next
    return True

def linkedListPal2(head):
    fast = head
    slow = head
    slowPrev = Head
    while fast!=None and fast.next != None:
        fast = fast.next.next
        slowPrev = slow
        slow = slow.next
    reverse(slow)
#alternative method - reverse the list in halves, check if first half is equal to the second half
