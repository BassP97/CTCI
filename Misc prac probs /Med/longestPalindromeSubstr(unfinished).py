"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""
def checkSubstr(toCheck):
    matchingSubstr = []
    currPopIndex = len(toCheck)
    for i in range(0, len(toCheck)):
        if (i<(len(toCheck)/2)):
            matchingSubstr.append(toCheck[i])
        else:
            if matchingSubstr[-1]!=toCheck[i]:
                return False
            else:
                matchingSubstr.pop(-1)
    return True

def main(toCheck):
    currLongest = ""
    for i in range(0,len(toCheck)):
        locNextChar = toCheck.find(toCheck[i], i+1)
        #print("checking:", toCheck[i:locNextChar+1], "between ", i,locNextChar, " after checking for",toCheck[i])
        if locNextChar!=-1:
            if checkSubstr(toCheck[i:locNextChar+1]):
                #print(toCheck[i:locNextChar+1], " is a palindrome")
                if (len(toCheck[i:locNextChar+1])>len(currLongest)):
                    currLongest = toCheck[i:locNextChar+1]
    print(currLongest)
    return currLongest

assert(checkSubstr("abccba") == True)
assert(checkSubstr("abcccba") == False)
assert(main("babba") == "abba")
assert(main("babbbbab")=="babbbbab")
assert(main("cbbd") == "bb")
