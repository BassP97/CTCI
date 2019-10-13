
def matchParens(inputStr):
    queue = []
    for paren in inputStr:
        print(queue, paren)
        if paren == ")":
            if queue[-1] == "(":
                del queue[-1]
        elif paren == "}":
                del queue[-1]
        elif paren == "]":
            if queue[-1] == "[":
                del queue[-1]
        elif paren == "(" or paren == "[" or paren == "(":
            queue.append(paren)
        else:
            return False
    return len(queue) == 0
assert(matchParens("[(])")==False)
assert(matchParens("[]()")==True)
