"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that
cover all the numbers in the array exactly. That
is, each element of nums is covered by exactly
one of the ranges, and there is no integer x
such that x is in one of the ranges but not in
nums.
"""


def summaryRanges(nums):
    if len(nums) < 1:
        return []
    res = []
    prev = nums[0]
    start = nums[0]
    for num in nums[1:]:
        if num > prev+1:
            if start != prev:
                res.append(str(start)+"->"+str(prev))
            else:
                res.append(str(start))
            start = num
        prev = num
    if start != prev:
        res.append(str(start)+"->"+str(prev))
    else:
        res.append(str(start))
    return res


print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([1]))
