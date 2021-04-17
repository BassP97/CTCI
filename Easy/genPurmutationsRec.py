"""
Write a recursive function for generating all permutations of an input 
string. Return them as a set. Assume every char in the string is unique
"""

def genPerms(string):
    if len(string)<=0:
        return set([string])
    temp = string[:-1]
    char = string[-1]
    permSet = genPerms(temp)
    retSet = set()
    for item in permSet:
        for i in range(0,len(item)+1):
            retSet.add(item[:i]+char+item[i:])
    return retSet

print(genPerms("agbcasdf;asdfklasdfjkl;fjasdl;fjasdlkfsadkjlfjsdkadfsajkfsdajkdfasj;dsfajklfsdakl;jadfs;dfsdfsa;l"))
