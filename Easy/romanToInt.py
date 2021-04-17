"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as
XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However,
the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle
applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within
the range from 1 to 3999.
"""
def romanConv(romanNum):
    total = 0
    minOneFlag = False
    minTenFlag = False
    minHundredFlag = False
    romanDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(0,len(romanNum)):
        if i!=len(romanNum)-1 and not(minOneFlag or minTenFlag or minHundredFlag):
            if romanNum[i] == "I":
                if romanNum[i+1] == "V" or romanNum[i+1] == "X":
                    minOneFlag = True
                    continue
            elif romanNum[i] == "X":
                if romanNum[i+1] == "L" or romanNum[i+1] == "C":
                    minTenFlag = True
                    continue
            elif romanNum[i] == "C":
                if romanNum[i+1] == "D" or romanNum[i+1] == "M":
                    minHundredFlag = True
                    continue

        currNum = romanDict[romanNum[i]]
        if minOneFlag:
            currNum = currNum-1
        if minTenFlag:
            currNum = currNum-10
        if minHundredFlag:
            currNum = currNum-100

        print currNum,romanNum[i]
        total = total+currNum
    print(total)
    return total


romanConv("III")
romanConv("IV")
romanConv("LVIII")
