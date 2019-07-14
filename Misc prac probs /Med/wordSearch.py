"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter
cell may not be used more than once.
"""

https://leetcode.com/problems/word-search/

def main(board, word):
    potentialStart = []
    for i in range(0, len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] == word[0]:
                potentialStart.append((i,j))

    for startLoc in potentialStart:
        currLoc = startLoc
        for i in range(0,len(word)+1):
            print(i)
            try:
                if (board[currLoc[0]+1][currLoc[1]])==word[i]:
                    currLoc = (currLoc[0]+1,currLoc[1])
            except IndexError:
                pass
            try:
                if (board[currLoc[0]-1][currLoc[1]])==word[i]:
                    currLoc = (currLoc[0]-1,currLoc[1])
            except IndexError:
                pass

            try:
                if (board[currLoc[0]][currLoc[1]+1])==word[i]:
                    currLoc = (currLoc[0],currLoc[1]+1)
            except IndexError:
                pass

            try:
                if (board[currLoc[0]-1][currLoc[1]-1])==word[i]:
                    currLoc = (currLoc[0],currLoc[1]-1)
            except IndexError:
                pass

            try:
                if (i == len(word)):
                    return True
            if
    return False

assert(main([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED") == True)

assert(main([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "SEE") == True)

assert(main([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB") == True)
