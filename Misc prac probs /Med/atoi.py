"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect
on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
"""

def main(toConvert):
    numVector = []
    neg = False
    numSet = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    convertedNum = 0

    for char in toConvert:
        if char == "-":
            neg = True
        elif char in numSet:
            numVector.append(char)
        else:
            if len(numVector) == 0 and char != " ":
                return 0

    for i in range(0, len(numVector)):
        currNum = numVector[i]
        asciiNum = ord(currNum)
        #convert this ascii number to a base ten number, then multiply that
        #base ten number by a power of ten depending on its relevant location in the string
        baseTenNum = asciiNum-48
        multFactor = len(numVector)-1-i
        finalDigit = baseTenNum*(10**multFactor)
        convertedNum += finalDigit
        
    if neg == True:
        convertedNum = convertedNum - (2*convertedNum)
    return convertedNum

assert(main("55")==55)
assert(main("-55")==-55)
