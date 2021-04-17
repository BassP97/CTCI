"""
Given an array of non-negative integers, you are initially 
positioned at the first index of the array.

Each element in the array represents your maximum jump 
length at that position.

Determine if you are able to reach the last index.
"""

#greedy solution - inverted iteration means that we keep track of the earliest index we can reach from the final index
#if that ends up being zero, then we're good. If it doesn't, then we're not

#intuition: this is kinda like a "wave" - if a given entry can land anywhere inside the "wave" then we can expand to emcompass it
#this is, functionally, moving the endpoint further and further forward, reducing the problem size
def jumpGame(nums):
    earliestIndex = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        print(earliestIndex,i,nums[i], i+nums[i])
        if i+nums[i]>=earliestIndex:
            earliestIndex = i
    print(earliestIndex)
    return earliestIndex == 0

assert(jumpGame([2,3,1,1,4]) == True)
assert(jumpGame([3,2,1,0,4]) == False)