"""
Given a non-empty array containing only positive integers, find if the array can be 
partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.
"""

def partSubSum(arr):
    arrSum = 0
    for num in arr:
        arrSum = num+arrSum
    if arrSum%2 == 1 or max(arr)>arrSum/2:
        return False
    target = arrSum//2
    dp = [False]*(target+1)
    dp[0] = True
    for num in arr:
        for i in range(target,num-1,-1):
            if dp[i-num] == True:
                dp[i] = True
    return dp[target]
    
    

assert(partSubSum([1, 5, 11, 5]) == True)
assert(partSubSum([1, 2, 3, 5]) == False)