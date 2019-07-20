"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longComPre(wordsToCheck):
    print("start")
    isCommon = True
    currIndex = 0
    prefix = ""
    smallestWordSize = 1000
    for word in wordsToCheck:
        if len(word)<smallestWordSize:
            smallestWordSize = len(word)
    while (isCommon and currIndex <= smallestWordSize-1):
        currLetter = wordsToCheck[0][currIndex]
        for word in wordsToCheck:
            if word[currIndex]!=currLetter:
                print(prefix)
                return prefix
        prefix = prefix+currLetter
        currIndex = currIndex+1
    return prefix

assert(longComPre(["flower","flow","flight"]) == "fl")
assert(longComPre(["dog","racecar","car"]) == "")
