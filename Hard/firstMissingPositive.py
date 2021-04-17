"""
Given an unsorted integer array, find the smallest missing positive integer.

Solution must run in O(n) time and use constant extra space
"""

#version w/ hash table (satisfies O(n) time but not constant extra space)
def findSmallPosInt(arr):
    print "goin on ", arr
    intHash = {}
    max = arr[0]
    intHash[arr[0]]=True
    for i in arr[1:]:
        if i>max:
            max = i
        intHash[i] = True

    for i in range(1,max):
        if i not in intHash.keys():
            return i
    return max+1



print findSmallPosInt([1,2,0])
print findSmallPosInt([3,4,-1,1])
print findSmallPosInt([7,8,9,11,12])
