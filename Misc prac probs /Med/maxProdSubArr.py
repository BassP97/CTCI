"""
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
#if no zero, must be an array starting at front or starting at end 
#quick proof: imagine we have arr in the middle from i to j. Consider arr[i-1] and arr[j+1]. If both are negative, 
#we can add both and expand. If one is positive, we can add it. If both are, we also add both
#because we add SOMETHING no matter what, eventually we reach front or end
def maxProdSubArr(nums):
    #reverse nums
    arrB = nums[::-1]
    arrA = nums
    maxA = float("-inf")
    maxB = float("-inf")
    for i in range(1,len(nums)):
        print(arrA, arrB)
        if arrB[i] != 0:
            arrB[i] = arrB[i-1]*arrB[i]
            if arrB[i]>maxB:
                maxB = arrB[i]
        else:
            arrB[i] = 1
        if arrA[i] != 0:
            arrA[i] = arrA[i-1]*arrA[i]
            if arrA[i]>maxA:
                maxA = arrA[i]
        else:
            arrA[i] = 1
    return max(maxA, maxB)
        


print(maxProdSubArr([2,3,-2,4]))