"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
For input, let -1 denote null


Solution doesn't compile but is correct - I'm too lazy to implement a tree
but the solution stands conceptually
"""


"""
Algorithm:

Traverse tree recursively in pre-order, returning the value of the current node to
the above recursion level. When recieving returns from lower levels, check left
and right return values are equal. If not, return a pre determined value that will
keep returning up until it reaches the root. If the root recieves that value, it will
return -1 (or false)
"""
