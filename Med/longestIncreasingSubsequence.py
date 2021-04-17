"""
Given an unsorted array of integers,
find the length of longest increasing subsequence.
"""

def main(arr):
    maxAtCurrLoc = []
    currMaxRet = 0
    for i in range(0,len(arr)):
        currMaxLen = 0
        for j in range(0,i):
            #if the Ith value is greater than the Jth value, assume the Ith value is in the max increasing subsequence 
            #else, Jth value's longest increasing subseq and append our Ith value on to that
            if arr[i]>arr[j]:
                currMaxLen = max(currMaxLen, maxAtCurrLoc[j])
        currMaxLen = currMaxLen+1
        if currMaxLen>currMaxRet:
            currMaxRet=currMaxLen
        maxAtCurrLoc.append(currMaxLen)
    return currMaxRet


assert(main([10,9,2,5,3,7,101,18]) == 4)
