"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.
"""
def main(input, dict):
    currinput = ""
    seg = [False for i in range(len(input)+1)]
    seg[0] = True
    for i in range(0,len(input)+1):
        for j in range(i):
            print(input[j:i])
            if ((seg[j]) and (input[j:i] in dict)):
                print(i)
                seg[i] = True
    print(seg)
    return seg[len(input)];


assert(main("leetcode",["leet","code"])==True)
assert(main("applepenapple",["apple","pen"])==True)
assert(main("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)
