"""
Given a sorted array nums, remove the duplicates in-place such that each element
appear only once and return the new array.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.
"""

def removeDups(sortedArr):
    currIndex = 0
    while(currIndex!=len(sortedArr)-1):
        while(sortedArr[currIndex]==sortedArr[currIndex+1]):
            del sortedArr[currIndex]
        currIndex = currIndex+1
    return sortedArr

print(removeDups([1,1,2]))
print(removeDups([0,0,1,1,1,2,2,3,3,4]))
