"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number
0 itself.

Again, too lazy to actually implement a linked list but here's the algorithm
"""

def reverseLL(currNode, prevNode):
    if currNode.next == NULL:
        currNode.next = prevNode
        head = currNode
        return
    reverse(currNode->next,currNode)
    currNode.next = prevNode
    return



#assumptions - each list has two or more items in it
def addNumsLL(head1,head2):
    reverseLL(head1, null)
    reverseLL(head2, null)
    carry = 0
    while(head1 != null):
        temp = head1.value + head2.value
        nextCarry = 0

        if temp >= 10:
            nextCarry = temp-10
            temp = temp-10
        toAdd = temp+carry

        if toAdd >= 10:
            nextCarry = nextCarry + (toAdd-10)
            toAdd = toAdd-10

        head1 = toAdd
        carry = nextCarry

        if head1.next == null and carry != 0:
            #create a new node with value zero
            head1.next = newNode(0)
            newNode = carry
            break
    reverseLL(head1,null)
    return head1
