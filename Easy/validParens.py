"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""

def validParens(parenStr):
    stack = []
    for i in parenStr:
        if (i == '(' or i == '{' or i == '['):
            stack.append(i)
        else:
            temp = stack.pop()
            if (temp == '(' and i !=')'):
                return False
            elif (temp == '{' and i !='}'):
                return False
            elif (temp == '[' and i !=']'):
                return False
    return len(stack) == 0


assert(validParens("()[]{}") == True)
assert(validParens("((()(())))") == True)
assert(validParens("()[") == False)
