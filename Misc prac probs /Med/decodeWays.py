"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""

def main(decodeStr):
    totalWays = 0
    decodeWays = [1]
    prevVal1or2 = (decodeStr[0] == 1 or decodeStr[0] == 2)
    for i in range(1,len(decodeStr)):
        if decodeStr[i] < 6 and prevVal1or2:
            decodeWays.append(decodeWays[i-1]*2)
        else:
            decodeWays.append(decodeWays[i-1]+1)
        prevVal1or2 = (decodeStr[i] == 1 or decodeStr[i] == 2)
        
    return decodeWays[len(decodeStr)-1]
assert(main("12")==2)
assert(main("226")==3)
