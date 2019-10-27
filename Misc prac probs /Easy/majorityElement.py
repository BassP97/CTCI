"""
Given an array of size n, find the majority element. The majority element is the element that 
appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement(arr):
    majorityElem = {}
    for item in arr:
        if item in majorityElem.keys():
            majorityElem[item] = majorityElem[item]+1
            if majorityElem[item] >= len(arr)//2:
                return item
        else:
            majorityElem[item] = 1