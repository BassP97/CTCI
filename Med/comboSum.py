"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""


def combinationSum4(nums, target):
    if not nums:
        return 0
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for i in range(1, target+1):
        last = [x for x in nums if x <= i]
        dp[i] = sum(dp[i-x] for x in last)
    return dp[-1]
