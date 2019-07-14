import copy
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a
transformed word.
"""

def canTransform(str1,str2):
    if len(str1)!=len(str2):
        print('len not equal')
        return False
    oneDiff = False
    for i in range(0,len(str1)):
        if (str1[i]!=str2[i] and not(oneDiff)):
            oneDiff = True
        elif (str1[i]!=str2[i] and oneDiff):
            return False
    return oneDiff


def wordLadder(wordList, beginWord, endWord):
    prevWords = [beginWord]
    for n in range(0,len(wordList)+1):
        nextWords = []
        for i in wordList:
            for j in prevWords:
                if canTransform(j,i):
                    nextWords.append(i)
                    if j in wordList:
                        wordList.remove(j)
                    if i == endWord:
                        return n+1
                        
        prevWords = copy.deepcopy(nextWords)
    print("cant find thing")
    return -1

assert(wordLadder(["hot","dot","dog","lot","log","cog"], "hit", "cog") == 5)
