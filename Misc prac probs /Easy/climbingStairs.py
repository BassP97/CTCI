"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Note: Given n will be a positive integer.
"""

def climbStairs(numStairs):
    if numStairs == 1:
        return 1
    if numStairs == 2:
        return 2
    stairArr = [1,2]
    for i in range(2,numStairs):
        stairArr.append(stairArr[i-1]+stairArr[i-2])
    print(stairArr)
    return stairArr[numStairs-1]
assert(climbStairs(3)==3)
