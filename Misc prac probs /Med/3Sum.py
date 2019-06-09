"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""


#assuming sumArray always contains 3 or more elements
def main(sumArray):
    if (len(sumArray) == 3):
        if(sumArray[0]+sumArray[1]+sumArray[2]==0):
            return([subArray[0], subArray[1], subArray[2])
        return
    else:
        copyArray = []
        for i in range(0, len(sumArray)):
            copyArray = sumArray[0:i] + sumArray[i+1:]
            main(copyArray)



main([-1, 0, 1, 2, -1, -4])
