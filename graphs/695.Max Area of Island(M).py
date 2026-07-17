from typing import List
"""
My Solution

use dfs to traverse each island, and use global counter to compare each area of island

check
can we modify the grid
how big is the grid
will there be any number other than 1, 0

Time:
O(MN), M = len(grid), N = len(grid[0])

Space:
stack worst O(MN)

"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])
        self.count = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] != 1:
                return 
            
            grid[r][c] = 0
            self.count += 1
            dfs(r-1, c) 
            dfs(r+1, c) 
            dfs(r, c-1)
            dfs(r, c+1) 
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    dfs(i, j)
                    ans = max(ans, self.count)
                    self.count = 0
        return ans

"""
Optimize

use return value to replac global value, it will be more clean, and not to worry forget to reset count
and return value basically is bottom-up, if use self.count, it's a top-down method, it's not tuitive
only if the ans will happen in any node of the tree, then we can use a global var. to collect

Time:
O(MN), M = len(grid), N = len(grid[0])

Space:
stack worst O(MN)
"""

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            count = 1
            count += dfs(r-1, c) 
            count += dfs(r+1, c) 
            count += dfs(r, c-1)
            count += dfs(r, c+1)

            return count
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
