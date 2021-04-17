"""
Given an integer array nums of unique elements, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


def subsetsInner(nums, n):
    if n == 0:
        return [[]]
    subsets = subsetsInner(nums, n-1)
    res = []
    seen = set()
    for subset in subsets:
        res.append(subset)
        for num in nums:
            if num not in subset and frozenset(subset+[num]) not in seen and len(subset) == n-1:
                res.append(subset+[num])
                seen.add(frozenset(subset+[num]))
    return res


def powerSet(nums):
    return subsetsInner(nums, len(nums))


def increment(binaryList):
    for i in range(len(binaryList)-1, -1, -1):
        if binaryList[i] != 1:
            binaryList[i] = 1
            for j in range(i+1, len(binaryList)):
                binaryList[j] = 0
            break
    return binaryList


def binaryNumToSet(nums, binaryList):
    res = []
    for num, binDigit in zip(nums, binaryList):
        if binDigit == 1:
            res.append(num)
    return res


def incrementMethod(nums):
    binaryList = []
    res = []
    for num in nums:
        binaryList.append(0)
    for i in range(pow(2, len(nums))):
        print(binaryList)
        res.append(binaryNumToSet(nums, binaryList))
        binaryList = increment(binaryList)
    return res


print(incrementMethod([1, 2, 3]))
