def revStr(string):
    if len(string) == 0:
        return ""
    return string[len(string)-1]+ revStr(string[:len(string)-1])

#doesn't work because strings are immutable in python lol, would if they weren't
def revStr2(string):
    for i in range(len(string)//2):
        temp = string[i]
        string[i] = string[len(string)-i-1]
        string[len(string)-i-1] = temp
    return string
    
print(revStr2("testStr"))