"""
Given a string s, partition s such that every substring of the partition is a
palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aabb"
Output:
[
  ["aabb"]
  ["aa","bb"],
  ["a","a","bb"]
  ["aa","b","b"]
]
"""

"""
This takes O(n*2^n) time,
For a string with length n, there will be (n - 1) intervals between chars.
For every interval, we can cut it or not cut it, so there will be 2^(n - 1) ways to partition the string.
For every partition way, we need to check if it is palindrome, which is O(n).
So the time complexity is O(n*(2^n))

Notes: Treat possible partitions as nodes on a tree - root is no partition - ie
whole string. Each of its children have one partition - ie they divide the string
into two chunks. The root has (n-1) children (w/ string length n). Each string then
has children partitioning the right string chunk - so at most n-2 children.

For every node, we check the last item of the list and iterate through the ways we
can partition it. If any of those partition options create a list in which the last
two items are palindromes, we add that to our list. For any partition options whose
left partition is a palindrome, we create a partition object using said partition,
and recursively call our partition function on our new object. Rinse repeat
"""
import copy

def isPalindrome(string):
    mid = False
    stack = []
    if len(string)%2 != 0:
        mid = True
    for i in range(0,len(string)//2):
        stack.append(string[i])
    startLoc = len(string)//2
    if mid:
        startLoc = startLoc+1
    for i in range(startLoc, len(string)):
        if stack.pop()!=string[i]:
            return False
    return True


retArr = []
def partitionInternal(currPartition):
    if len(currPartition[-1]) == 1:
        return
    for i in range(1,len(currPartition[-1])):
        if isPalindrome(currPartition[-1][0:i]):
            newPartition = copy.deepcopy(currPartition)
            palOne = currPartition[-1][0:i]
            palTwo = currPartition[-1][i:]
            newPartition.pop()
            newPartition.append(palOne)
            newPartition.append(palTwo)
            if isPalindrome(currPartition[-1][i:]):
                if newPartition not in retArr:
                    retArr.append(newPartition)
            partitionInternal(newPartition)

def partitionPalindromes(inputStr):
    partitionInternal([inputStr])
    return retArr

partitionPalindromes("bannab")
