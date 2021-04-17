"""
Given a non-empty array of integers, every element appears 
twice except for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. 
    Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4
"""

def singleNumExtraMem(arr):
    seen = set()
    res = 0
    for num in arr:
        if num not in seen:
            res+=(num*2)
            seen.add(num)
    return res-sum(arr)

#when we xor two nums together, we get 0. So xoring everything in our array 
#leaves us with whatever number only appears once
def singleNumNoExtra(arr):
    res = 0
    for num in arr:
        res ^= num
    return res 
assert(singleNumNoExtra([4,1,2,1,2]) == 4)
assert(singleNumNoExtra([2,2,1]) == 1)