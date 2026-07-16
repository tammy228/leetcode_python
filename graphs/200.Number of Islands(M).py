from typing import List
"""
Optimize

use for each island, use dfs to traverse all the island

check
will there be other number than 0, 1
how big is the grid

Time:
O(MN), M for len(grid), N for len(grid[0])

Space:
worst O(MN) for recursion stack
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] != "1":
                return
            
            grid[r][c] = "0" # indicate visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans