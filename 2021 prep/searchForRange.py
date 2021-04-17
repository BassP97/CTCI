"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""


def searchRange(nums, target, lo, hi, left=True):
    if lo == hi:
        return -1
    mid = lo+((hi-lo)//2)
    if nums[mid] == target and left:
        if mid == 0 or nums[mid-1] < target:
            return mid
        return searchRange(nums, target, lo, mid, left)
    if nums[mid] == target and not left:
        if mid == len(nums)-1 or nums[mid+1] > target:
            return mid
        return searchRange(nums, target, mid+1, hi, left)
    if nums[mid] < target:
        return searchRange(nums, target, mid+1, hi, left)
    return searchRange(nums, target, lo, mid, left)


def searchRangeWrapper(nums, target):
    return [searchRange(nums, target, 0, len(nums)), searchRange(nums, target, 0, len(nums), False)]


assert(searchRangeWrapper([5, 7, 7, 8, 8, 10], 8) == [3, 4])
assert(searchRangeWrapper([5, 7, 7, 8, 8, 10], 6) == [-1, -1])
assert(searchRangeWrapper([], 0) == [-1, -1])
print('all tests passed')
