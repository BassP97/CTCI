"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line
i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.
"""

def findConBrute(containerArr):
    start = 0
    end = 0
    currMaxWater = 0

    for i in range(0, len(containerArr)):
        for j in range(i, len(containerArr)):
            currWater = min(containerArr[i], containerArr[j])*(j-i)
            if currWater>currMaxWater:
                currMaxWater = currWater
    print currMaxWater
    return currMaxWater

def findConEff(containerArr):
    left = 0
    right = len(containerArr)-1
    currMaxWater = 0

    while (left!=right):
        currWater = min(containerArr[left], containerArr[right])*(right-left)
        if currWater>currMaxWater:
            currMaxWater = currWater

        if left<right:
            left = left+1
        if right<left:
            right = right-1
    return currMaxWater
    
findConEff([1,8,6,2,5,4,8,3,7])
