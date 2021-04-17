"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 

Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

"""

from bisect import bisect_left


def lengthOfLISDP(nums):
    if not nums:
        return 0
    n = len(nums)
    f = [0] * n
    for i in range(n):
        max_lis = 0
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                max_lis = max(max_lis, f[j])
        f[i] = max_lis + 1
    return max(f)


def lengthOfLISBSDP(nums):
    dp = []
    for i in range(len(nums)):
        print(dp)
        pos = bisect_left(dp, nums[i])
        if pos == len(dp):
            dp.append(nums[i])
        else:
            dp[pos] = nums[i]
    return len(dp)


assert(lengthOfLISBSDP([10, 9, 2, 5, 3, 4, 7, 101, 18]) == 5)
