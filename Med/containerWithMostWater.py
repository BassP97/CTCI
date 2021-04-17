"""
Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical height 
are drawn such that the two endpoints of line i is at (i, ai) 
and (i, 0). Find two height, which together with x-axis forms 
a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

def contMostWater(height):
    left = 0
    right = len(height)-1
    currMax = 0
    while left!=right:
        currContainerVolume = min(height[left],height[right])*(right-left)
        if currContainerVolume > currMax:
            currMax = currContainerVolume
        if height[left]<height[right]:
            left = left+1
        else:
            right = right-1
    return currMax

print(contMostWater([1,8,6,2,5,4,8,3,7]))
