# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
from collections import deque
"""
My Solution

use bfs level order, return only last element of the level

ex:
[]
[1]
left skew, right skew

Time:
O(N)

Space:
O(W), worst O(N)

"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q, ans = deque([root]), []
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i == level_size - 1:
                    ans.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return ans
    
"""
dfs

right side first, only consider first node

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root, depth):
            if not root:
                return None
            
            if len(ans) == depth:
                ans.append(root.val)

            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        
        dfs(root, 0, ans) # int is Immutable, if recursive call it will copy the var.
        return ans