"""
Calculate the sum of two integers a and b,
but you are not allowed to use the operator + and -.
"""


def binListToNum(toConvert):
    currNum = 0
    for i in toConvert:
        currNum = currNum ^ i
        currNum = currNum << 1
    currNum = currNum >> 1
    return currNum

# crappy way of getting an integer to a binary vector


def numToBinList(toConvert):
    return [int(x) for x in bin(toConvert)[2:]]

# note: assumes we don't have to account for overflow
# also assumes both numbers have the same number of bits - big flaw, fix later


def main(num1, num2):
    carry = 0
    numList1 = numToBinList(num1)
    numList2 = numToBinList(num2)
    maxLen = max(len(numList1), len(numList2))
    resArr = []
    for i in range(maxLen-1, -1, -1):
        res1 = numList1[i] ^ numList2[i]
        carry1 = numList1[i] & numList2[i]
        realRes = carry ^ res1
        carry2 = res1 & carry
        carry = carry1 | carry2
        resArr.insert(0, realRes)
    if carry == 1:
        resArr.insert(0, 1)
    toReturn = binListToNum(resArr)
    return toReturn


assert(main(8, 11) == 19)
assert(main(7, 5) == 12)
assert(main(14, 9) == 23)
