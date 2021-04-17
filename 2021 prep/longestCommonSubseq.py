def longestCommonSubseqReq(seq1, seq2):
    if seq1[-1] == seq2[-1]:
        return longestCommonSubseqReq(seq1[:len(seq1)-1], seq2[:len(seq2)-1])+1
    return max(longestCommonSubseqReq(seq1[:len(seq1)-1], seq2), longestCommonSubseqReq(seq1, seq2[:len(seq2)-1]))


def printList(res):
    for l in res:
        print(l)


def longestCommonSubseq(seq1, seq2):
    res = [[0 for i in range(len(seq2))] for j in range(len(seq1))]
    if seq1[0] == seq2[0]:
        res[0][0] = 1
    for i in range(len(res)):
        for j in range(len(res[0])):
            isEqual = (seq1[i] == seq2[j])
            toAdd = 0
            if isEqual:
                print("have ", seq1[i], seq2[j], " in common at ", i, j)
                toAdd += 1
                if i > 0 and j > 0:
                    res[i][j] = res[i-1][j-1]+toAdd
                else:
                    res[i][j] = 1
            elif i > 0 and j > 0:
                res[i][j] = max(res[i][j-1], res[i-1][j])
            elif i > 0:
                res[i][j] = res[i-1][j]
            elif j > 0:
                res[i][j] = res[i][j-1]

    return res[len(seq1)-1][len(seq2)-1]


print(longestCommonSubseq("abcde", "ace"))
print(longestCommonSubseq("abc", "def"))
print(longestCommonSubseq("bsbininm", "jmjkbkjkv"))
