"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class parens(object):
    returnSet = []
    def createParens(self, n):
        self.createParensRec("", n, 0, 0)
        print(self.returnSet)
        return self.returnSet

    def createParensRec(self, currSol, n, numStartParens, numEndParens):
        if numStartParens+numEndParens == 2*n:
            self.returnSet.append(currSol)
            return
        elif numStartParens==numEndParens:
            self.createParensRec(currSol+"(",n,numStartParens+1,numEndParens)
        elif numStartParens>numEndParens:
            self.createParensRec(currSol+")",n,numStartParens,numEndParens+1)
            if numStartParens<n:
                self.createParensRec(currSol+"(",n,numStartParens+1,numEndParens)

parenObj = parens()
assert(parenObj.createParens(4) == [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
])
