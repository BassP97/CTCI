"""
Given an array nums of n integers, are there elements 
a, b, c in nums such that a + b + c = 0? Find all 
unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
"""


def threeSum(arr):
    sumSet = {}
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if (i+j) not in sumSet.keys():
                sumSet[i+j] = []
            sumSet[i+j].append(i)
            sumSet[i+j].append(j)
    retArr = []
    for i in range(0, len(arr)):
        if arr[i] in sumSet.keys():
            retArr.append([i]+sumSet[i])
    return retArr
