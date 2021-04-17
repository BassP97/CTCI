"""
Given a non-empty array of digits representing a non-negative integer, plus one
to the integer.

The digits are stored such that the most significant digit is at the head of the
list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

def plusOne(intArr):
    carry = False
    for i in range(len(intArr)-1,-1,-1):
        if carry == True or i == len(intArr)-1:
            intArr[i] = intArr[i]+1
        if intArr[i] >= 10:
            carry = True
            intArr[i] = 0
            if intArr[i] == 11:
                intArr[i] += 1
        else:
            break
    print(intArr)
plusOne([1,2,3])
plusOne([4,3,2,1])
plusOne([4,3,9,9])
