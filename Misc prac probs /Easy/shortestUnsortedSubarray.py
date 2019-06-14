"""
Given an integer array, you need to find one continuous subarray that if
you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
"""

#assumes list values are between -1 and 100
def main(toCheck):
    prevVal=-1
    currLoc = 0
    min = 100
    max = -1
    startLoc = 0
    endLoc = len(toCheck)-1
    flag = False
    for i in toCheck:
        if i > prevVal:
            prevVal = i
        else:
            flag = True
        if flag == True:
            if i < min:
                min = i
    flag = False
    prevVal = 100
    currLoc = len(toCheck)-1
    for i in reversed(toCheck):
        if i < prevVal:
            prevVal = i
        else:
            flag = True
        if flag == True:
            if i > max:
                min = i

    for i in range(0, len(toCheck)-1):
        if min<toCheck[i]:
            startLoc = i
            break
    for i in range(len(toCheck)-1, 0, -1):
        if max>toCheck[i]:
            endLoc = i
            break
    return endLoc - startLoc


assert(main([2, 6, 4, 8, 10, 9, 2, 6, 7, 15]) == 8)
