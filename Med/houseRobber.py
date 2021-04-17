"""
You are a professional robber planning to rob nums along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent nums have 
security system connected and it will automatically contact the 
police if two adjacent nums were broken into on the same night.

Given a list of non-negative integers representing the amount of 
money of each house, determine the maximum amount of money you 
can rob tonight without alerting the police.
"""
def robber(nums):
    dp = []
    for i in range(len(nums)):
        if i-2>=0:
            if max(dp[i-2]+nums[i],dp[i-1]) == dp[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2]+nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)

#order: prev2, prev1, num
def alternate(nums):
    prev1 = 0
    prev2 = 0
    for num in nums:
        temp = prev1
        prev1 = max(prev2+num,prev1)
        prev2 = temp
    return prev1

print(alternate([13300,111000,2,23,100]))