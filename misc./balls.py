"""

"""

def findNumBalls(numBalls,numBins):
    if numBins == 1:
        return 1
    else:
        temp = numBalls
        for i in range(0,numBalls):
            temp = temp*findNumBalls(numBalls-i,numBins)
        return temp

print(findNumBalls(2,2))
