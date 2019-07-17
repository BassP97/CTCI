"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

def reverseInt(toReverse):
    strRev = str(toReverse)
    toReturn = ""
    neg = False
    for digit in strRev:
        if digit == "-":
            neg = True
        else:
            toReturn = digit+toReturn

    returnVal = int(toReturn)
    if neg:
        returnVal = returnVal*-1
    print returnVal
    if returnVal < -2**31 or returnVal > (2**31) - 1:
        return 0
    return returnVal

assert(reverseInt(32) == 23)
assert(reverseInt(121) == 121)
assert(reverseInt(-32) == -23)
assert(reverseInt(120)== 21)
