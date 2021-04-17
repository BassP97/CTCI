"""
Given an array of non-negative integers, you are initially
positioned at the first index of the array.

Each element in the array represents your maximum jump
length at that position.

Determine if you are able to reach the last index.
"""

def main(toCheck):
    returnArr = [False]*len(toCheck)
    returnArr[0] = True
    for i in range(0,len(toCheck)):
        if i+toCheck[i] <= len(returnArr)-1 and returnArr[i]:
            returnArr[toCheck[i]+i] = True
        if i-toCheck[i] >= 0 and returnArr[i]:
            returnArr[i-toCheck[i]] = True
            i = i-toCheck[i]-1
        print returnArr
    return returnArr[len(toCheck)-1]

assert(main([2,3,1,1,4]) == True)
print("================ ")
assert(main([3,2,1,0,4]) == False)
