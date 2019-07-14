"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes first.
"""
#note - it would be better to do this with a priority queue but some languages dont have heaps
#       one so this shitty priority queue with a dictionary will have to do

#priority queue would be  O(n) time while this is O(n logn) time cuz of the sort
def main(wordList, k):
    wordDict = {}
    for i in wordList:
        if i in wordDict.keys():
            wordDict[i] = wordDict[i]+1
        else:
            wordDict[i] = 1

    wordFreq = []
    for i in wordDict.keys():
        wordFreq.append((i, wordDict[i]))

    wordFreq.sort(key=lambda x: x[1], reverse = True)

    returnArr = []
    for i in range(0,k):
        returnArr.append(wordFreq[i][0])
    return returnArr

assert(main(["i", "love", "leetcode", "i", "love", "coding"],2) == ["i", "love"])
assert(main(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"])
