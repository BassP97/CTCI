"""
Given an array of integers, return indices of the 
two numbers such that they add up to a specific target.

You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

Example:
"""

def twoSum(nums, target):
    targHash = {}
    for i in range(0,len(nums)):
        if (target-nums[i]) in targHash.keys():
            return [i,targHash[target-nums[i]]]
        targHash[nums[i]] = i
    return 