"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png
"""
keyPadMapping = {}
keyPadMapping["2"] = ['a','b','c']
keyPadMapping["3"] = ['d','e','f']
keyPadMapping["4"] = ['g','h','i']
keyPadMapping["5"] = ['j','k','l']
keyPadMapping["6"] = ['m','n','o']
keyPadMapping["7"] = ['p','q','r','s']
keyPadMapping["8"] = ['t','u','v']
keyPadMapping["9"] = ['w','x','y','z']
keyPadMapping["0"] = [' ']

def main(numSeq):
    results = keyPadMapping[numSeq[0]]
    for i in numSeq[1:]:
        newResults = []
        for j in results:
            for k in keyPadMapping[i]:
                newResults.append(j+k)
        print(newResults)
        results = newResults
    return results

assert(main("234") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
