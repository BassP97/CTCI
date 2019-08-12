"""
Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.
"""

def findLargestRec(bar,hist):
    left = bar
    doneLeft = False
    right = bar
    doneRight = False
    while not(doneLeft and doneRight):
        if not doneLeft:
            left = left-1
            if left<0 or hist[left]<hist[bar]:
                left = left+1
                doneLeft = True
        if not doneRight:
            right = right+1
            if right>len(hist)-1 or hist[right]<hist[bar]:
                doneRight = True
    recSize = (right-left)*hist[bar]
    return recSize

#n^2 approach
def largeRecHistBrute(hist):
    largestRec = 0
    for bar in range(0,len(hist)):
        recAtCurrBar = findLargestRec(bar,hist)
        if recAtCurrBar>largestRec:
            largestRec = recAtCurrBar
    return largestRec



assert(largeRecHistBrute([2,1,5,6,2,3]) == 10)
