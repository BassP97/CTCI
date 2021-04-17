"""
Given a string s, find the length of the longest substring without
repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Example 4:

Input: s = ""
Output: 0

"""


def longestSubstringWithoutRepeatingChars(s):
    if len(s) == 1:
        return 1
    lo = 0
    curr = 0
    maxLen = 0
    locMap = {}
    while curr < len(s):
        if s[curr] in locMap.keys():
            # here we do the max to avoid re-introducing already eliminated elements
            # for instance, with "abba", we move lo to the second 'b', but upon encountering
            # the second 'a' we (without the max) move it back down to the first 'a' at index 0
            # resulting in a bad return value of 3
            lo = max(lo, locMap[s[curr]]+1)
        locMap[s[curr]] = curr
        curr += 1
        if curr-lo > maxLen:
            maxLen = curr-lo
    return maxLen


assert(longestSubstringWithoutRepeatingChars("abcabcbb") == 3)
assert(longestSubstringWithoutRepeatingChars("bbbbb") == 1)
assert(longestSubstringWithoutRepeatingChars("pwwkew") == 3)
assert(longestSubstringWithoutRepeatingChars("") == 0)
assert(longestSubstringWithoutRepeatingChars("abba") == 2)
