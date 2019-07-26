"""
Given two integers dividend and divisor, divide two integers without using
multiplication, division and mod operator.

Return the quotient after dividing dividend(x) by divisor(y).

The integer division should truncate toward zero.
"""

#returning x/y
def divide(x, y):
    if x<0 or y<0:
        x = abs(x)
        y = abs(y)
        neg = True
    currShiftVal = 1
    shiftDiv = y
    quotient = 0
    neg = False
    multVal = 1
    while x>y:
        if x-shiftDiv>=0:
            shiftDiv = shiftDiv<<1
            currShiftVal = currShiftVal<<1
        else:
            x = x-(shiftDiv>>1)
            currShiftVal = currShiftVal>>1
            quotient = quotient + currShiftVal
            shiftDiv = y
            currShiftVal = 1
    if neg:
        quotient = quotient*-1
    print "returning:",quotient,"\n"
    return quotient

divide(10,3)
divide(7,-3)
divide(90,5)
divide(80,4)
