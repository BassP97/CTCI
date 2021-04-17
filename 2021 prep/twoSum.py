def twoSum(nums, target):
    numLoc = {}
    for i, num in enumerate(nums):
        if num in numLoc.keys():
            return [i, numLoc[num]]
        numLoc[target-num] = i


assert(set(twoSum([2, 7, 11, 15], 9)) == set([0, 1]))
