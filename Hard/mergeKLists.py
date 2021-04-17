"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""

#assumes all list have elements < 100000
def mergeLists(listOfNodeHeads):
    currListHead = new node()
    currListNode = newListHead.next()
    currListLoc = []
    for i in range(0,len(nodeHeads)):
        currListLoc.append(listOfNodeHeads[i])
    for item in range(0,len(listOfNodeHeads)):
        currMax = 100000
        for i in currListLoc:
            if i<currMax:
                minNode = i
                currMax = i.value
        currListNode.next = minNode
        currListNode = minNode
    temp = currListHead
    currListHead = temp.next
    delete temp
    return currListHead
