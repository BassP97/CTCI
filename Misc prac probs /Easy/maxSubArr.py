"""
Given an integer array nums, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
import sys
def maxSubArr(nums):
    currSum = 0
    left = 0
    right = 0
    prevMax = 0
    maxArr = []
    while (left!=right or right!=len(nums)-1):
        print(left, right, currSum, nums[left:right+1])
        if left < right and right<len(nums)-1 and currSum - nums[left] > currSum + nums[right+1]:
            currSum = currSum - nums[left]
            left = left+1
        else:
            currSum = currSum + nums[right]
            right = right+1
        if currSum > prevMax:
            prevMax = currSum
            maxArr = nums[left:right+1]
        if right>len(nums)-1:
            break
    return sum(maxArr)

"""
intuition:
If the prev sum subarray is positive, its sum will possibly "benefit" curritem
If the prev sum is negative, it wont benefit curritem, so we toss it and restart the array

at the end, find the max array sum
"""
def sumDP(nums):
    for i in range(1,len(nums)):
        if nums[i-1]>0:
            nums[i] = nums[i]+nums[i-1]
    return max(nums)

print(sumDP([-2,1]))