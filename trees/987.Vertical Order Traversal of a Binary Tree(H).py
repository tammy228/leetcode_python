# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
from collections import defaultdict
"""
My Solution

for tree we can use top-down dfs to collect each node with their column, and use a hash map to record the node

Time:
dfs:  O(N)
map iteration+sorted: worst O(N) + O(N/2 log N/2)
total: O(NlogN)

Space:
auxiliary: map + stack + result = O(N)+ worst O(N) + O(N/2) = O(N)
auxiliary + output = O(N) + O(N) = O(N)
"""
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map = defaultdict(list)
        self.min_col = float('inf')
        ans = []
        # dfs traversal with col
        def dfs(root, row, col):
            if not root: return None

            if col < self.min_col: self.min_col = col
            map[col].append((row, root.val))
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
        
        dfs(root, 0, 0)

        # for i in range(self.min_col, self.min_col + len(map)):
        #     result = sorted(map[i])
        #     ans.append([x[1] for x in result])
        for col in sorted(map.keys()):
            result = sorted(map[col])
            ans.append([x[1] for x in result])
        return ans 
        