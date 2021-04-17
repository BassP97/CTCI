"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence
of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""


def longestIncreasingSubseq(arr):
    res = [1 for i in range(len(arr))]
    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr[:i]):
            if num1 > num2:
                res[i] = max(res[i], res[j]+1)
    return max(res)


assert(longestIncreasingSubseq([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
assert(longestIncreasingSubseq([0, 1, 0, 3, 2, 3]) == 4)
assert(longestIncreasingSubseq([7, 7, 7, 7, 7, 7, 7]) == 1)
