"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:

Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:

    Elements of the given array are in the range of 0 to 10^9
    Length of the array will not exceed 10^4.
"""

def hammingDist(num1,num2):
    binNum1 = format(num1, "32b")
    binNum2 = format(num2, "32b")
    hamming = 0
    for i in range(len(binNum1)):
        if binNum1[i] != binNum2[i]:
            hamming+=1
    return hamming

def sumAllHamming(numArr):
    hamming = 0
    for i in range(0,len(numArr)):
        for j in range(i,len(numArr)):
            hamming = hamming+hammingDist(numArr[i],numArr[j])
    return hamming

def countBits(num1):
    ret = 0
    while(num1!=0):
        ret += num1&1
        num1>>1
    return ret

def betterSol(numArr):
    numStrArr = []
    hamming = 0
    for num in numArr:
        binNum = format(num, "032b")
        numStrArr.append(binNum)
    for i in range(0,32):
        numZeroes = 0
        numOnes = 0
        for num in numStrArr:
            if num[i]=="0":
                numZeroes+=1
            else:
                numOnes+=1
        hamming += (numZeroes*numOnes)
    return hamming

if __name__ == "__main__":
    print(betterSol([4, 14, 2]))