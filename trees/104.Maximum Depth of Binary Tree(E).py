# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
My Solution

use dfs to find the tree depth, if there the node is none, then return 0,
for one level tree, it will be 1 + max(L, R)

Time:
O(N)

Space:
O(H), H for tree height, worst O(N), avg O(logN)
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)