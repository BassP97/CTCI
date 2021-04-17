"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.
"""

def anagrams(strs):
    strDict = {}
    keys = set()
    retArr = []
    for str in strs:
        temp = tuple(sorted(list(str)))
        if temp in keys:
            strDict[temp].append(str)
        else:
            keys.add(temp)
            strDict[temp] = [str]
    for key in keys:
        retArr.append(strDict[key])
    
    return retArr

def countingAnagrams(strs):
    strDict = {}
    keys = set()
    retArr = []
    for str in strs:
        currCount = []
        for i in range(26):
            currCount.append(0)
        for c in str:
            currCount[ord(c)-ord('a')]+=1
        keyArr = tuple(currCount)
        if keyArr in keys:
            strDict[keyArr].append(str)
        else:
            keys.add(keyArr)
            strDict[keyArr] = [str]
    for key in keys:
        retArr.append(strDict[key])
    return retArr
    
print(countingAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))