"""
Given an integer array nums, in which exactly two elements 
appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?
"""


def singleNumber(self, nums):
    tmp = 0
    for num in nums:
        tmp ^= num
    i = 0
    while tmp & 1 == 0:
        tmp >>= 1
        i += 1
    tmp = 1 << i
    first, second = 0, 0
    for num in nums:
        if num & tmp:
            first ^= num
        else:
            second ^= num
    return [first, second]
