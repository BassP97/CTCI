"""
Given a list of integers, find the highest product you can get from three of the integers.

The input nums will always have at least three integers.
"""
def prodThree(nums):
    if len(nums)<3:
        raise ValueError("Should have three nums")
    high = max(nums[0], nums[1])
    low  = min(nums[0], nums[1])
    highProd2 = nums[0] * nums[1]
    lowProd2  = nums[0] * nums[1]
    highProd3 = nums[0] * nums[1] * nums[2]
    for num in nums[2:]:
        highProd3 = max(highProd3,highProd2*num,lowProd2*num)
        highProd2 = max(highProd2, high*num)
        lowProd2 = min(lowProd2,low*num,high*num)
        high = max(high, num)
        low = min(low,num)
    return highProd3
print(prodThree([1, 10, -5, 1, -100]))
