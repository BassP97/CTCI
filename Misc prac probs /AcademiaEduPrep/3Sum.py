"""
Given an array nums of n integers, are there elements a, b, c in nums such that 
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def threeSumSet(nums):
    if len(nums)<3:
        return []
    numSet = {}
    indicesSet = {}
    for i,num in enumerate(nums):
        for j,num2 in enumerate(nums[i+1:]):
            temp = -1*(num+num2)
            if temp in numSet.keys():
                numSet[temp].append([num,num2])
                indicesSet[temp].append([i,j+i+1])
            else:
                numSet[temp] = [[num,num2]]
                indicesSet[temp] = [[i,j+i+1]]
    inSet = set()
    sol = []
    for i,num in enumerate(nums):
        if num in numSet.keys():
            for n,need in enumerate(numSet[num]):
                currCoord = indicesSet[num][n]
                if i not in currCoord:
                    temp = need+[num]
                    if frozenset(temp) not in inSet:
                        sol.append(temp)
                        inSet.add(frozenset(temp))
    return sol
    
print(threeSumSet([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
