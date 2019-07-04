"""
Given n non-negative integers representing an elevation map where
the width of each bar is 1, compute how much water it is able to
trap after raining.
"""

def main(topography):
    interStart = 0
    interEnd = 0
    intervalList = []
    i = 0
    #step one - get all the intervals that will be filled with water
    while(i!=len(topography)-1):
        if topography[i] > 0:
            interStart = i
            interEnd = 0
            for j in range(i+1,len(topography)):
                if topography[j] >= topography[i]:
                    interEnd = j
                    break
            if interEnd != 0:
                intervalList.append((interStart,interEnd))
                i = j
            else:
                i = i+1
        else:
            i = i +1
        print i

    #step 2 - subtract the underwater elevations from the total volume of our intervals
    totalVol = 0
    for pair in intervalList:
        #get interval volume
        currVol = min(topography[pair[0]],topography[pair[1]]) * (pair[1]-pair[0]-1)
        #subtract underwater volume from interval volume
        for i in range(pair[0]+1, pair[1]):
            currVol = currVol - topography[i]
        totalVol = totalVol+currVol

    return totalVol


assert(main([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
