"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

note - too lazy to implement linked list, pseudo-code will have to do
"""

def reverse(currNode,prevNode):
    if currNode.next == NULL:
        currNode.next = prevNode
        return
    reverse(currNode->next,currNode)
    currNode.next = prevNode
    return
