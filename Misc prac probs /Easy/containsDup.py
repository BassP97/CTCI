"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.
"""

#uses constant space, O(n log n) time
def constSpace(toCheck):
    toCheck.sort()
    print(toCheck)
    for i in range(0, len(toCheck)-1):
        if toCheck[i] == toCheck[i+1]:
            return True
    return False


#uses O(n) space, O(n) time
def main(toCheck):
    inArr = {}
    for i in toCheck:
        if i in inArr.keys():
            return True
        inArr[i] = True
    return False

assert(constSpace([1,2,3,1]) == True)
assert(constSpace([1,2,3,4]) == False)
assert(constSpace([1,1,1,3,3,4,3,2,4,2]) == True)
