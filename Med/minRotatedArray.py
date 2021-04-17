"""
Suppose an array sorted in ascending order is rotated 
t some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
def minRotatedArray(nums):
    #edge case - arrays of two or fewer numbers
    if len(nums)<=2:
        return min(nums)
    left = 0
    right = len(nums)-1
    
    #if array hasn't been pivoted
    if nums[left]<nums[right]:
        return nums[left]
    
    while right-left>1:
        mid = left+((right-left)//2)
        print(mid, left, right ,nums[left:right+1])
        if nums[mid]<=nums[left]:
            right = mid
        if nums[mid]>nums[left]:
            left = mid
    return min(nums[right],nums[left])
print(minRotatedArray([3,4,5,1,2]))
print(minRotatedArray([4,5,6,0,1,2]))