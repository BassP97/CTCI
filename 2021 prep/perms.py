"""
Given an array nums of distinct integers, return all the 
possible permutations. You can return the answer in any order.
"""

from time import sleep


def perms(arr):
    if len(arr) == 1:
        return [arr]
    subPerms = perms(arr[1:])
    res = []
    print('subperms', subPerms)
    for perm in subPerms:
        print('perm:', perm)
        for i in range(len(perm)+1):
            temp = perm[:i]+[arr[0]]+perm[i:]
            print('prefix:', perm[:i])
            print('suffix:', perm[i:])
            print('appending', temp)
            res.append(temp)
    print('post subperms', res)
    return res


print(perms([1, 2, 3]))
