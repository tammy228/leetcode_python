from typing import List
from collections import deque
"""
My Solution 

for each rotting orange we need to traverse with BFS at the same time
and count how many fresh oranges left with each iteration

Time:
O(MN)

Space:
worst for deque is O(MN)
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    cr, cc = r+dr, c+dc
                    if 0 <= cr < len(grid) and 0 <= cc < len(grid[0]) and grid[cr][cc] == 1:
                        q.append((cr, cc))
                        grid[cr][cc] = 2
                        fresh -= 1
            time += 1
            if fresh == 0:
                break
        return time if not fresh else -1    
