"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.


Example 1:

Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


def findPeak(nums, l, r):
    if r == l:
        return r
    mid = ((r-l)//2)+l
    # if we hit an edge and it's a peak, return said peak
    if (mid == 0 and nums[1] < nums[mid]) or (mid == len(nums)-1 and nums[len(nums)-1] < nums[mid]):
        return mid
    # if we hit a peak
    if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
        return mid
    if nums[mid-1] > nums[mid]:
        return findPeak(nums, l, mid)
    return findPeak(nums, mid+1, r)


def peakWrapper(nums):
    if len(nums) <= 2:
        return max(nums)

    return findPeak(nums, 0, len(nums)-1)


assert(peakWrapper([2, 1, 2]) == 0 or peakWrapper([2, 1, 2]) == 2)

"""
assert(peakWrapper([1, 2, 1, 3, 5, 6, 4]) ==
       1 or peakWrapper([1, 2, 1, 3, 5, 6, 4]) == 5)
assert(peakWrapper([1, 2, 3, 1]) == 2)
assert(peakWrapper([1, 2, 3]) == 2)
"""
