# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
My Solution

use dfs to check subtree heights and return false if height diff more than 1

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # return height
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0
            
            left = dfs(curr.left)
            if left == -1:
                return -1
            
            right = dfs(curr.right)
            if right == -1:
                return -1

            if abs(left-right) > 1:
                return -1
            
            return max(left, right) + 1
        ans = dfs(root)
        return ans != -1

"""
use template, so no early stopping
""" 
class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return 1 + max(left, right)
        dfs(root)
        return self.ans
