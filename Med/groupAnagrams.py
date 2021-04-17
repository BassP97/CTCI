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
def createAnaList():
  ret = []
  for i in range(0,26):
    ret.append(0)
  return ret

def groupAna(anagramList):
  anaSet = {}
  retArr = []
  currSlot = 0
  for ana in anagramList:
    anaZeroes = createAnaList()
    for letter in ana:
      print(anaZeroes[ord(letter)-97])
      anaZeroes[ord(letter)-97] = anaZeroes[ord(letter)-97]+1
    if str(anaZeroes) not in anaSet.keys():
      anaSet[str(anaZeroes)] = currSlot
      currSlot = currSlot+1
      retArr.append([])
    retArr[anaSet[str(anaZeroes)]].append(ana)
  return retArr
print(groupAna(["eat", "tea", "tan", "ate", "nat", "bat"]))