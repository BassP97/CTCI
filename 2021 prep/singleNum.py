"""
Given a non-empty array of integers nums, every element
appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear 
runtime complexity and without using extra memory?
"""


def singleNum(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


assert(singleNum([2, 2, 1]) == 1)
assert(singleNum([1]) == 1)
assert(singleNum([4, 1, 2, 1, 2]) == 4)
