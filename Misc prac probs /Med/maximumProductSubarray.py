"""
Given an integer array nums, find the contiguous subarray within
an array (containing at least one number) which has the largest product.
"""
def prod(array):
    if len(array)>0:
        currTotal = array[0]
        for i in array[1:]:
            currTotal = currTotal*i
    else:
        currTotal = 0
    return currTotal
#brute force n^3, very bad!
def bruteForce(toCheck):
    currMax = -100000
    currSum = 0
    for i in range(len(toCheck)):
        if(i>currMax):
            currMax = i
        for j in range(i+1, len(toCheck)):
            currSum = prod(toCheck[i:j])
            if (currSum>currMax):
                currMax = currSum
    return currMax

def better(toCheck):
    negNumLoc = [[]]
    zeroArrays = [[]]
    start = 0
    end = 0
    currMax = toCheck[0]
    #find all zeroes in the list and make sub arrays of the numbers between the
    #zeroes - this is because no array ought to contain a zero if there are
    #positive numbers available
    for i in range(0,len(toCheck)):
        end = i
        if toCheck[i] == 0:
            zeroArrays.append(toCheck[start:end])
            negNumLoc.append([])
            start = end+1
            currMax = 0
    zeroArrays.append(toCheck[start:])
    negNumLoc.append([])

    for i in range(0, len(zeroArrays)):
        ispos = False
        evenNeg = True
        for j in range(0, len(zeroArrays[i])):
            if zeroArrays[i][j]>0:
                isPos = True
            else:
                evenNeg = not(evenNeg)
                negNumLoc[i].append(j)

        if evenNeg:
            checkVal = prod(zeroArrays[i])
        else:
            temp = zeroArrays[i]
            withoutFirstVal = prod(temp[negNumLoc[i][0]+1:])
            withoutLastVal = prod(temp[:negNumLoc[i][-1]])
            checkVal = max(withoutLastVal,withoutLastVal)
        if checkVal>currMax:
            currMax = checkVal
    return currMax



arr1 = [2,3,-2,4]
arr2 = [-2,0,-1]
assert(better(arr1) == 6)
assert(better(arr2) == 0)
