"""
Given an array of non-negative integers nums,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum
jump length at that position.

Determine if you are able to reach the last index.
"""


def jumpGame(nums):
    reachArr = [False for i in range(len(nums))]
    reachArr[0] = True
    reachedThusFar = 0
    for i, num in enumerate(nums):
        if i > reachedThusFar:
            return False
        reachedThusFar = max(reachedThusFar, i+num)
        print(reachedThusFar)
    return True


assert(jumpGame([2, 3, 1, 1, 4]) == True)
assert(jumpGame([3, 2, 1, 0, 4]) == False)
assert(jumpGame([2, 0]) == True)
