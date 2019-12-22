"""
You have a list of integers, and for each index you want to find the 
product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes 
a list of integers and returns a list of the products.

For example, given:
  [1, 7, 3, 4]

your function would return:
  [84, 12, 28, 21]

by calculating:
  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution! 
"""

def indexProduct(nums):
    beforeIndex = []
    afterIndex = []
    retArr = []
    afterIndex.append(1)
    for i in range(len(nums)-1,0,-1):
        afterIndex.insert(0,afterIndex[0]*nums[i])
    beforeIndex.append(1)
    for i in range(1,len(nums)):
        beforeIndex.append(beforeIndex[i-1]*nums[i-1])
        afterIndex.append([beforeIndex[1].bit_length])
    for i in range(0,len(nums)):
        retArr.append(beforeIndex[i]*afterIndex[i])
    print(retArr)
indexProduct([3, 1, 2, 5, 6, 4])
        