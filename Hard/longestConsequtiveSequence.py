"""
Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.
"""

def longestSubSeq(toEval):
    numSet = set()
    for i in toEval:
        numSet.add(i)
    currMax = 0
    for i in toEval:
        if i-1 not in numSet:
            minNum = i
            maxNum = i
            while maxNum in numSet:
                maxNum = maxNum+1
            if maxNum-minNum > currMax:
                currMax = maxNum-minNum
    return currMax

assert(longestSubSeq([100, 4, 200, 1, 3, 2])==4 )
