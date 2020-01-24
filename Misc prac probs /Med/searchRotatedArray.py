"""
Suppose an array sorted in ascending order is rotated at 
some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the 
array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order 
of O(log n).
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

def binSearch(arr, target, left, right):
    mid = left+((right-left)//2)
    if mid == target:
        return target
    if left == right:
        return -1
    if arr[mid]<target:
        return binSearch(arr, target, mid+1, right)
    return binSearch(arr, target, left, mid-1):

def searchArr(arr, target):
    start = minRotatedArray(array)
    if target < arr[left]:
        return binSearch(arr[start:],target, start, len(arr)-1)
    return binSearch(arr[0:start], target, 0, start-1)
    