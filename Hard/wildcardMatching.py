"""
Given an input string (s) and a pattern (p), implement wildcard pattern
matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
"""


def matchStr(pattern,inputStr):
    #if both inputs are of length 0, we're done!
    if len(inputStr)==0 and len(pattern)==0:
        return True
    # Make sure that there exist characters after '*' in the input string
    # This is what stops us once we go too far in patern matching w/ *
    if len(pattern)>1 and pattern[0]=="*" and len(inputStr) == 0:
        return False

    #if the current character in our pattern is "?" or both characters match,
    #check the next character
    if (len(pattern)>0 and pattern[0]=="?") or len(inputStr)>0 and (len(pattern)>0 and (pattern[0]==inputStr[0])):
        return matchStr(pattern[1:],inputStr[1:])

    # If there is *, then there are two possibilities
    # a) We consider current character of second string
    # b) We ignore current character of second string.
    if len(pattern)>0 and pattern[0] == "*":
        return matchStr(pattern[1:],inputStr) or matchStr(pattern,inputStr[1:])

    return False

assert(matchStr("a","aa")==False)
assert(matchStr("*","aa")==True)
assert(matchStr("*a*b","adceb")==True)
