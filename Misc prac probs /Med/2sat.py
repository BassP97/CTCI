"""
Given an array equations of strings that represent relationships between variables, 
each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  
There is no way to assign the variables to satisfy both equations.

Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
"""
import collections

def twoSat(clauses):
    equalSet = {}
    notEqualSet = {}
    for clause in clauses:
        if (clause[1:3]=="!="):
            if clause[0] in notEqualSet.keys():
                notEqualSet[clause[0]].add(clause[3])
            else:
                notEqualSet[clause[0]] = set(clause[3])

            if clause[3] in notEqualSet.keys():
                notEqualSet[clause[3]].add(clause[0])
            else:
                notEqualSet[clause[3]] = set(clause[0])

            if clause[0] in equalSet.keys():
                equalSet[clause[0]].update(notEqualSet[clause[0]])
                if clause[3] in equalSet[clause[0]]:
                    return False
            if clause[3] in equalSet.keys():
                equalSet[clause[3]].update(notEqualSet[clause[3]])
                if clause[0] in equalSet[clause[3]]:
                    return False
        else:
            if clause[0] in equalSet.keys():
                equalSet[clause[0]].add(clause[3])
            else:
                equalSet[clause[0]] = set(clause[3])

            if clause[3] in equalSet.keys():
                equalSet[clause[3]].add(clause[0])
            else:
                equalSet[clause[3]] = set(clause[0])   

            if clause[0] in notEqualSet.keys():
                notEqualSet[clause[0]].update(equalSet[clause[0]])
                if clause[3] in notEqualSet[clause[0]]:
                    return False
            if clause[3] in notEqualSet.keys():
                notEqualSet[clause[3]].update(equalSet[clause[3]])
                if clause[0] in notEqualSet[clause[3]]:
                    return False 
                
    return True

assert(twoSat(["a==b","b!=a"]) == False)
assert(twoSat(["a==b","b==c","a==c"]) == True)
assert(twoSat(["a==b","b!=c","c==a"]) == False)
assert(twoSat(["c==c","b==d","x!=z"]) == True)
