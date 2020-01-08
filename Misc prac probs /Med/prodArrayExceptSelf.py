"""
Given an numsay nums of n integers where n > 1,  return an array 
output such that output[i] is equal to the product of all the 
elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output 
numsay does not count as extra space for the purpose of space 
complexity analysis.)
"""
def prodArrExceptSelf(nums):
    if len(nums) == 0:
        return []
    leftHand = []
    rightHand = []
    output = []
    rightHand.append(1)
    leftHand.append(1)
    for i in range(1,len(nums)):
        rightHand.append(rightHand[i-1]*nums[i-1])
    for i in range(len(nums)-2,-1,-1):
        leftHand.insert(0,leftHand[0]*nums[i+1])
    for i in range(0,len(nums)):
        output.append(leftHand[i]*rightHand[i])
    return output

def prodArrExceptSelfConstSpace(nums):
    if len(nums) == 0:
        return []
    output = []
    output.append(1)
    for i in range(1,len(nums)):
        output.append(output[i-1]*nums[i-1])
    temp = 1
    for i in range(len(nums)-1,-1,-1):
        print(nums[i],temp,output)
        output[i] = temp * output[i]
        temp = temp*nums[i]
    return output
print(prodArrExceptSelfConstSpace([1,2,3,4]))