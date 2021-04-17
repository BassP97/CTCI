"""
Given n pairs of parentheses, write a function to
generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]


"""

from collections import deque


def isValid(toCheck):
    stack = deque()
    for char in toCheck:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def genParensInner(curr, leftToPlace, leftPlaced, rightPlaced):
    print(curr)
    if leftToPlace == 0 and rightPlaced == leftPlaced:
        return [curr]
    res = []
    if leftToPlace > 0:
        res += genParensInner(curr+'(', leftToPlace-1,
                              leftPlaced+1, rightPlaced)
    if leftPlaced > rightPlaced:
        res += genParensInner(curr+')', leftToPlace, leftPlaced, rightPlaced+1)
    return res


def genParens(n):
    return genParensInner('', n, 0, 0)


assert(set(genParens(3)) == set(
    ["((()))", "(()())", "(())()", "()(())", "()()()"]))

assert(set(genParens(4)) == set(["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
                                 "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]))
