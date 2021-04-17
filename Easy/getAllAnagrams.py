"""
Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.
"""
def makeListOfChars(p):
    charInP= set()
    for char in p:
        charInP.add(char)
    return charInP

#O(m*n) time, not great but not awful
def main(s, p):
    charInP = makeListOfChars(p)
    listOfIndices = []
    for i in range(0, len(s)):
        print(s[i])
        if (len(charInP) > len(s)-i):
            break
        if (s[i] in charInP):
            charInP.discard(s[i])
            length = len(charInP)
            for currIndex in range(1, length+1):
                if s[i+currIndex] in charInP:
                    charInP.discard(s[i+currIndex])
                else:
                    break
            if len(charInP) == 0:
                listOfIndices.append(i)
            charInP = makeListOfChars(p)
    print(listOfIndices)
    return listOfIndices


assert(main("cbaebabacd", "abc") == [0, 6])
assert(main("abab", "ab") == [0, 1, 2])
