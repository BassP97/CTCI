"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the number that is missing from the array.
"""

def main(toCheck):
    min = 0
    max = 0
    #get the range to check
    for i in toCheck:
        if i > max:
            max = i
    checklist = {}
    for i in range(0,max+1):
        checklist[i] = i
    for i in toCheck:
        checklist.pop(i)
    returnVal = 0
    for item in checklist:
        returnVal = item
    print(returnVal)
    return returnVal

def alternative(toCheck):
    sumAll = len(toCheck)
    sumToCheck = 0
    for i in range(0,len(toCheck)):
        sumAll = sumAll+i
        sumToCheck = sumToCheck+toCheck[i]
    return(sumAll-sumToCheck)

assert(alternative([3,0,1]) == 2)
assert(alternative([9,6,4,2,3,5,7,0,1])==8)
