"""
A s containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1: 

    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
def doesCorrespond(digits):
    temp = int(digits)
    if temp>=10 and temp<=26:
        return True
    return False

def decodeWays(s):
    correspWays = [0]*(len(s)+1)
    if len(s)==1:
        if s[0]!="0":
            return 1
        return 0
    correspWays[0] = 1
    if s[1]!=0:
        correspWays[1] = 1
    if doesCorrespond(s[0]+s[1]) and (s[0]+s[1] != "10"):
        correspWays[1] = 2
    for i in range(2,len(s)):
        if s[i]!="0":
            correspWays[i] += correspWays[i-1]
        if s[i]!="0" and int(s[i-1]+s[i])<=26:
            correspWays[i] += correspWays[i-2]
    print(correspWays)
    return correspWays[len(s)]

print(decodeWays("226"))
print(decodeWays("12"))