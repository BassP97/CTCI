"""
 Given a string S of '(' and ')' parentheses, we add the minimum number of 
 parentheses ( '(' or ')', and in any positions ) so that the resulting 
 parentheses string is valid.

Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to 
make the resulting string valid.
"""

def minAddParens(parenStr):
    open = 0
    needParens = 0
    for i in parenStr:
        if i == "(":
            open += 1
        else:
            if open!=0:
                open -= 1
            else:
                needParens+=1
    return needParens+open

assert(minAddParens("())") == 1)
assert(minAddParens("(((") == 3)
assert(minAddParens("()") == 0)
assert(minAddParens("()))((")==4)
print("we good")

