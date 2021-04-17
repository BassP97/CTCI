"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
def subseq(ints):
    if len(ints)==1:
        return [ints]
    res = []
    for i in range(len(ints)):
        arrWithouti = ints[:i] + ints[i+1:]
        allSubseqWithouti = subseq(arrWithouti)
        for seq in allSubseqWithouti:
            temp = [ints[i]]+seq
            res.append(temp)
    return res

listPrinter(subseq([1,2,3,4]))