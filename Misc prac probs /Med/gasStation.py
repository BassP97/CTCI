"""
There are N gas stations along a circular route, where the amount of gas at
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty
tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once
in the clockwise direction, otherwise return -1.

Note:

    If there exists a solution, it is guaranteed to be unique.
    Both input arrays are non-empty and have the same length.
    Each element in the input arrays is a non-negative integer.

Example 1:

Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
"""

#brute force solution
def gas(gas,cost):
    for startLoc in range(0,len(gas)):
        currGas = 0
        for currLoc in range(0,len(gas)+1):
            print ("startLoc:",startLoc,"Travel to station",(startLoc+currLoc)%len(gas),"your tank:",currGas,"-",cost[(startLoc+currLoc)%len(gas)],"+",gas[(startLoc+currLoc)%len(gas)])
            currGas = currGas - cost[(startLoc+currLoc)%len(gas)]
            currGas = currGas + gas[(startLoc+currLoc)%len(gas)]
            if currGas<0:
                break
            if (startLoc+currLoc)%len(gas)==startLoc and currLoc!=0:
                return startLoc
    return -1

#nonBrute solution
def gas(gas,cost):
    if sum(gas) < sum(cost):
        return -1
    else:
        for i in range(0,len(gas)):
            

assert(gas([1,2,3,4,5], [3,4,5,1,2]) == 3)
assert(gas([2,3,4],[3,4,3])==-1)
