"""
Given a s s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.
"""

def palindromicSubstring(s):
    prevBest = 0
    longestSubstring = ''
    for i in range(len(s)):
        for j in range(2):
            if j == 1:
                left = i
                right = i+1
            else:
                left = right = i
            while (left>=0 and right<len(s)) and s[left] == s[right]:
                left-=1
                right+=1
            left+=1
            right-=1
            if right-left>=prevBest:
                prevBest = right-left
                longestSubstring = s[left:right+1]
    return longestSubstring

assert(palindromicSubstring('abba') == 'abba')
assert(palindromicSubstring('abdcabbasdfadsf') == 'abba')
assert(palindromicSubstring())