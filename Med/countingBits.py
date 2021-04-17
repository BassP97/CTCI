"""
Given a non negative integer number num. For every numbers i in the
range 0 < i < num calculate the number of 1's in their binary representation
and return them as an array.
"""

#assumes num is non zero AND that num can be represented in 8 bits or less
#asymptotically this approach is O(N) since the cost of "rolling over" all
#the ones to zeroes gets amortized when the numbers get sufficiently large
def main(num):
    numOnes = 1
    numBits = 1
    firstZero = 0

    zeroLocs = [0]
    toReturn = [0]
    numOnes = [0]
    noZeroes = False
    for i in range(1,num+1):
        numOnes.append(0)
        #means we're "rolling over" from (2^n)-1 to 2^n
        if noZeroes:
            numBits = numBits+1
            noZeroes = False
            numOnes[i] = 1
            zeroLocs = []
            for j in range(0,numBits-1):
                zeroLocs.append(j)
            firstZero = 0
        else:
            #setting up a baseline
            numOnes[i] = numOnes[i-1]
            #rolling over all the 1s before the first zero to 0s
            numOnes[i] = numOnes[i] - firstZero
            #Add all our newly created zeroes to our list of zeroes
            for j in range(0, firstZero):
                zeroLocs.append(j)
            numOnes[i] = numOnes[i] + 1           #flipping the first zero to a 1
            zeroLocs.remove(firstZero)

            firstZero = 100000000
            for item in zeroLocs:
                if item<firstZero:
                    firstZero = item
            if firstZero == 100000000:
                noZeroes = True
        toReturn.append(numOnes[i])
    return toReturn

assert(main(2) == [0,1,1])
assert(main(5) ==[0,1,1,2,1,2])
assert(main(15)==[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4])
