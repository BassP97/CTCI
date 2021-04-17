"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


def llAdd(l1, l2):
    curr1 = l1
    curr2 = l2
    resHead = ListNode()
    resCurr = resHead
    carry = 0
    while curr1 != None or curr2 != None:
        if curr1 == None:
            resCurr.val = curr2.val
            curr2 = curr2.next
        if curr2 == None:
            resCurr.val = curr1.val
            curr1 = curr1.next
        else:
            resCurr.val = carry+curr1.val+curr2.val
            carry = 0
            if resCurr.val > 9:
                carry = 1
                resCurr = resCurr % 10
            curr1 = curr1.next
            curr2 = curr2.next
        resCurr = resCurr.next()

    if carry == 1:
        resCurr.val = 1
    return resHead


assert(llAdd([2, 4, 3], [5, 6, 4]) == [7, 0, 8])
assert(llAdd([0], [0]) == [0])
assert(llAdd([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1])
