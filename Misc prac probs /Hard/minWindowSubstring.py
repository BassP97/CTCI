"""
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

"""

#failed attempt
def minWindowSubstr(inputStr,toFind):
    inputSet = {}
    findSet = {}
    for i in inputStr:
        if i in inputSet.keys():
            inputSet[i] = inputSet[i]+1
        else:
            inputSet[i] = 1

    for i in inputStr:
        if i in findSet.keys():
            findSet[i] = findSet[i]+1
        else:
            findSet[i] = 1

    left = 0
    right = len(inputStr)-1

    while(left!=right):
        if (inputStr[left] not in findSet.keys()):
            left = left+1
        elif (inputStr[right] not in findSet.keys()):
            right = right-1
        else:
            #means we can't remove left or right strings because we need em
            print(inputSet[inputStr[left]])
            if inputSet[inputStr[left]] == findSet[inputStr[left]]:
                if inputSet[inputStr[right]] == findSet[inputStr[right]]:

            #if we can remove the left or right letters, do it
            if inputSet[inputStr[left]] == findSet[inputStr[left]]:
                inputSet[inputStr[right]] = inputSet[inputStr[right]]-1
                right = right-1
            if inputSet[inputStr[right]] == findSet[inputStr[right]]:
                inputSet[inputStr[left]] = inputSet[inputStr[left]]-1
                left = left+1
    if left == right:
        return ""
    else:
        for letter in inputStr[left:right]:
            if letter in findSet.keys():
                findSet[letter] = findSet[letter]-1
                if findSet[letter] == 0:
                    del findSet[letter]
            if findSet == {}
        if findSet!={}:
            return ""
        else:
            return inputStr[left:right]



print(minWindowSubstr("ADOBECODEBANC", "ABC"))
