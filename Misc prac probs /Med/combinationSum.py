"""
Given an integer array with all positive numbers and 
no duplicates, find the number of possible combinations 
that add up to a positive integer target.
"""

def comboSum(posArr,target):
    dp = [1]+[0]*target
    for num in posArr:
        dp[num]+=1
    for i in range(len(dp)):
        for num in posArr:
            if i-num>0 and dp[i-num]>0:
                dp[i] = dp[i]+dp[i-num]
    return dp[target]
