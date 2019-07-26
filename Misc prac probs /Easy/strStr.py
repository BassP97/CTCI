"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
"""

def findNeedle(needle, haystack):
    index = 0
    currNeedleLoc = 0
    while index!=len(haystack):
        if haystack[index] == needle[0]:
            found = True
            for i in range(1,len(needle)):
                if needle[i]!=haystack[index+i]:
                    found = False
                    break
            if found:
                return index
        index = index+1
    return -1
    
assert(findNeedle("ll","hello") == 2)
assert(findNeedle("bb","aaaa") == -1)
