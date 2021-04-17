"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""
from collections import Counter
def startAna(string, ana):
    anaCounter = Counter()
    for char in ana:
        anaCounter[char] += 1
    width = len(ana)
    currLoc = 0
    locs = []
    widthCounter = Counter()
    for char in string[0:currLoc+width]:
        widthCounter[char] += 1
    while True:
        if widthCounter == anaCounter:
            locs.append(currLoc)
        if currLoc + width >= len(string):
            break
        widthCounter[string[currLoc]] -= 1
        if widthCounter[string[currLoc]] == 0:
            del widthCounter[string[currLoc]]
        widthCounter[string[currLoc+width]] += 1
        currLoc = currLoc + 1
    return locs

print(startAna("abab", "ab"))

