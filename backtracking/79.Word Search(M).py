from typing import List
"""
My Solution

we can use backtracking to find the exact path to search word
for each position in board we need to search 4-direction
during the search we need to make sure the searching does not exceeded the boarder and also need to compare the word and also can not go backward
if the path match the length we can say we found it else no

each element in board
[A]
[AB] [AS]...
[ABF] [ABC]...

Time:
O(NM * 3^L), NM is board width and height, 3 is because we can not go backward, L for len(word)

Space:
auxiliary space: stack, O(L), L for len(word)
auxiliary space + output space: O(L)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != word[i]:
                return False

            board[r][c] = '#'

            found = (dfs(i+1, r+1, c) or
            dfs(i+1, r-1, c) or
            dfs(i+1, r, c-1) or 
            dfs(i+1, r, c+1))

            board[r][c] = word[i]
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(0, i, j): return True
        return False
        
