"""
Say you have an array for which the ith element is the price of a given stock on
day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

def main(toCheck):
    #assumes there is at least one number below 1000, and one above 0
    currMin = 1000
    minLoc = 0
    currMax = 0
    maxLoc = 0
    currProf = 0
    for i in range(1,len(toCheck)):
        if toCheck[i] > currMax:
            currMax = toCheck[i]
            maxLoc = i
    for i in range(0,maxLoc):
        print(currMin)
        if toCheck[i]<currMin:
            currMin = toCheck[i]
    if(currMin > currMax):
        return 0
    return(currMax - currMin)


assert(main([7,1,5,3,6,4]) == 5)
assert(main([7,6,4,3,1]) == 0)
