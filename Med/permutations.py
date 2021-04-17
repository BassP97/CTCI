"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def permutations(nums):
    if len(nums) == 1:
        return [nums]
    else:
        solArr = []
        for i in range(len(nums)):
            temp = nums[:i]+nums[i+1:]
            retPerms = permutations(temp)
            print(retPerms)
            for perm in retPerms:
                perm.insert(0,nums[i])
            solArr = solArr+retPerms
        return solArr
print(permutations([1,2,3,4,5]))