"""
Given an array of integers, return indices of the two numbers such
that they add up to a specific target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.
"""

#works in O(n) time and O(n) space
def main(toCheck,target):
    numNeeded = {}
    returnVal = []
    for i in range(0,len(toCheck)):
        if (toCheck[i] in numNeeded.keys()):
            returnVal.append(numNeeded[toCheck[i]])
            returnVal.append(i)
        else:
            numNeeded[target-toCheck[i]] = i
    print(returnVal)
    return returnVal


assert(main([2, 7, 11, 15], 9) == [0,1])
