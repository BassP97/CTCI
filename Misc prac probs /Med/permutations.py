"""
Given a collection of distinct integers, return all possible permutations.
"""
import copy

class permute(object):
    toRet = []

    def __init__(self):
        self.toRet = []

    def permWrapper(self, objs):
        toRet = []
        self.perm(objs, [])
        return toRet

    def perm(self, objs, currPerm):
        if len(objs) == 0:
            self.toRet.append(currPerm)
        else:
            for i in range(0,len(objs)):
                temp = copy.deepcopy(currPerm)
                temp.append(objs[i])
                self.perm(objs[0:i]+objs[i+1:],temp)
        print(self.toRet)

permObj = permute()
assert(permObj.permWrapper([1,2,3]))
