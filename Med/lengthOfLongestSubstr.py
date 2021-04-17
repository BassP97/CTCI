 def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        end = 0
        longest = 0
        letterDict = {}
        for i in range(len(s)):
            if s[i] in letterDict.keys():
                #we do this max thing because if start has moved forwards in between
                #seeing the current value last, that means that setting start to 
                #letterDict[s[i]]+1 would move it backwards, thus introducing duplicates
                start=max(letterDict[s[i]]+1, start)
            if i-start+1>longest:
                longest = i-start+1
            letterDict[s[i]]=i
        return longest