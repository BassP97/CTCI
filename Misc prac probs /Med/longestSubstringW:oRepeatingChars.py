import time
"""
Given a string, find the length of
the longest contiguous substring without repeating characters.
"""

#uses sliding window
def main(toCheck):
    start = 0
    end = 0
    maxLen = 0
    currChars = {}
    print("new")
    while(end<=len(toCheck)-1 and start <= len(toCheck)-1):
        char = toCheck[end]
        if not(char in currChars):
            currChars[toCheck[end]] = end;
            end = end+1
            if end-start > maxLen:
                maxLen = end-start
        else:
            del currChars[toCheck[start]]
            start = start+1
    return maxLen

assert(main("abcabcbb") == 3)
assert(main("bbbbb") == 1)
assert(main("pwwkew") == 3)
