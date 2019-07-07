"""
Given a non-empty array containing only positive integers, find if the array can
be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""


def main(set, partOne, partTwo):
    if len(set) == 0:
        print("yoot")
        if partOne == partTwo:
            return True
        return False
    else:
        inOne = partOne + set[0]
        inTwo = partTwo + set[0]
        removedSet = set[1:]
        return main(removedSet, inOne, partTwo) or main(removedSet, partOne, inTwo)

assert(main([1, 5, 11, 5], 0, 0) == True)
assert(main([1, 2, 3, 5], 0, 0) == False)
