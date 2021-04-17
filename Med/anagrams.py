"""
Given an array of strings, group anagrams together.
"""
import collections
#runtime O(m*nlogn) where m is the longest word length and n is the list size
def checkAnagrams(listOfWords):
    letterPools = {}
    retVal = []
    currIndex = 0
    for word in listOfWords:
        sortedWord = "".join(sorted(word))
        print word, sortedWord
        if sortedWord not in letterPools.keys():
            print sortedWord, "not in", letterPools
            letterPools[sortedWord] = currIndex
            retVal.append([word])
            currIndex = currIndex + 1
        else:
            retVal[letterPools[sortedWord]].append(word)
    print(retVal)

#better - runs in O(NM) time. Intuition: anagrams can be defined by the letter count in each word
def betterAnagrams(listOfWords):
    ans = collections.defaultdict(list)
    for word in listOfWords:
        letterCount = [0]*26
        for letter in word:
            letterCount[ord(letter)-ord('a')] += 1
        ans[tuple(letterCount)].append(word)
    print(ans.values())


checkAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
betterAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
