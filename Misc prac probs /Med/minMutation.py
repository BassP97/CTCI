"""
A gene string can be represented by an 8-character long string, with choices
from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"),
where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations.
A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the
minimum number of mutations needed to mutate from "start" to "end". If there is
no such a mutation, return -1.

Note:

    Starting point is assumed to be valid, so it might not be included in the bank.
    If multiple mutations are needed, all mutations during in the sequence must be valid.
    You may assume start and end string is not the same.
"""

def canTransform(string1, string2):
    oneChar = False
    if len(string1)!=len(string2):
        return False
    for i in range(0,len(ranstring1)):
        if string1[i]!=string2[i]:
            if oneChar:
                return False
            oneChar = True
    return oneChar

def traceBack(node):
    if node[1] == None:
        return 0
    else:
        return 1+node[1]

def bfs(adjMatrix, start, end):
    queue = deque()
    visited = {}
    for item in adjMatrix.keys():
        visited[item] = (False, None)
    visited[start] = True
    currNode = (start,None)
    while len(queue)!=0:
        if currNode == end:
            return traceback(currNode, adjMatrix)
        else:
            for i in adjMatrix[currNode[0]]:
                deque.appendLeft((i,currNode))
        currNode = queue.pop()
    return -1


def minMutation(bank,start,end):
    adjMatrix = {}
    for i in range(0,len(bank)):
        for j in range(i,len(bank)):
            if canTransform(bank[i],bank[j]):
                if i in adjMatrix.keys():
                    adjMatrix[bank[i]].add(bank[j])
                else:
                    adjMatrix[bank[i]] = set(bank[j])
                if j in adjMatrix.keys():
                    adjMatrix[bank[j]].add(bank[i])
                else:
                    adjMatrix[bank[j]] = set(bank[i])
    return bfs(adjMatrix, start, end)
