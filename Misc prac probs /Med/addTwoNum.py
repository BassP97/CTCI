"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

def addTwoNumWrapper(head1,head2):
    startHead = Node()
    addTwoNum(head1,head2,startHead)
    return startHead

def addTwoNum(head1, head2, startHead):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.next is None and head2.next is None:
        val = (head1.value+head2.value)%10
        nextNode = Node(val)
        startHead.next = Node
        if head1.value+head2.value >= 10:
            return 1
        else:
            return 0
    nextNode = Node()
    startHead.next = nextNode
    if head1.next is None:
        carryVal = addTwoNum(head1, head2.next, nextNode)
        val = head2.value+carryVal
    elif head2.next is None:
        carryVal = addTwoNum(head1.next,head2,nextNode)
        val = head1.value + carryVal
    else:
        carryVal = addTwoNum(head1.next,head2,next,nextNode)
        val = head1.value+head2.value+carryVal
    nextNode = val%10
    if val >=10:
        return 1
    return 0
