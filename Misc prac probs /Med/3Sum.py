"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""

def sumArr(array):
    currTotal = 0
    for i in array:
        currTotal = currTotal+i
    return currTotal

#recursive solution assuming sumArray always contains 3 or more elements
#does double count - so that's not great
def main(sumArray):
    if len(sumArray) == 3:
        if (sumArr(sumArray) == 0):
            print sumArray
    else:
        for i in range(0,len(sumArray)):
            main(sumArray[0:i]+sumArray[i+1:])



main([-1, 0, 1, 2, -1, -4])
