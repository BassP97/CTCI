"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

#sort by start values
def mergeSorting(intervalArr):
    intervalArr.sort(key=lambda startInt: startInt[0])
    retArr = []
    for i in intervalArr:
        if retArr == [] or retArr[-1][1]<i[0]:
            retArr.append(i)
        else:
            retArr[-1][1] = i[1]
    print(retArr)

#assumes lowest interval start is <1000000 and largest max is >0
def mergeNumLine(intervalArr):
    currMin = 1000000
    currMax = 0
    for i in intervalArr:
        if i[0]<currMin:
            currMin = i[0]
        if i[1]>currMax:
            currMax = i[1]

    numLine = [False]*(currMax)

    for i in intervalArr:
        for j in range(i[0],i[1]):
            numLine[j] = True

    inInt = False
    start = 0
    retArr = []

    for i in range(0,len(numLine)):
        if inInt and not numLine[i]:
            retArr.append([start,i])
            inInt = False
        if (not inInt) and numLine[i]:
            inInt = True
            start = i

    if inInt:
        retArr.append([start,currMax])
    print(retArr)

mergeNumLine([[1,3],[2,6],[8,10],[15,18]])
mergeNumLine([[1,4],[4,5]])

mergeSorting([[1,3],[2,6],[8,10],[15,18]])
mergeSorting([[1,4],[4,5]])
