"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
import string

def validPalin(toCheck):
    toCheck = toCheck.lower()
    toCheck = toCheck.replace(" ","")
    hasMid = False
    if len(toCheck)%2 == 1:
        hasMid = True
    halfLen = len(toCheck)//2
    letterStack = []
    for i in range(0,halfLen):
        letterStack.append(toCheck[i])
    if hasMid:
        halfLen = halfLen+1
    for i in range(halfLen,len(toCheck)):
        if toCheck[i]!=letterStack.pop():
            return False
    return True

assert(validPalin("A man a plan a canal Panama") == True)
assert(validPalin("race a car") == False)
assert(validPalin("Racecar") == True)
assert(validPalin("Red rum sir is murder") == True)
assert(validPalin("Eva can I see bees in a cave") == True)
