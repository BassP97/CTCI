"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another 
solution using the divide and conquer approach, which is more subtle.

"""
def maxSubArr(nums):
    curr = 0
    currMax = float('-inf')
    for i,num in enumerate(nums):
        if num>currMax:
            currMax = num
        if curr+num>0:
            nums[i] = curr+num
            curr = nums[i]
            if curr>currMax:
                currMax = curr
        else:
            curr = 0

        print(i,nums)
    return currMax
print(maxSubArr([-2,1,-3,4,-1,2,1,-5,4]))