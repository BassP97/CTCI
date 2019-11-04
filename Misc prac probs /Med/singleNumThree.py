"""
Given an array of numbers nums, in which exactly two elements appear only once and all 
the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:

    - The order of the result is not important. So in the above example, [5, 3] is also correct.
    - Your algorithm should run in linear runtime complexity. Could you implement it using 
    only constant space complexity?
"""
def singleNumThree(nums):
    xor = 0
    for num in nums:
        xor ^= num
    ret1=0
    ret2=0
    mask=1
    while (mask&xor == 0):
        mask = mask<<1
    for num in nums:
        if (num&mask):
            ret1 = ret1^num
        else:
            ret2 = ret2^num
        print(ret1,ret2)
    return((ret1,ret2))
print(singleNumThree([1,2,1,3,2,5]))