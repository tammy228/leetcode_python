# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
My Solution

use dfs to traversal both tree and compare each node

Time:
O(p+q)

Space:
O(ph + qh), worst O(p+q), , avg O(logq + logp)
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not p or not q or q.val != p.val:
            return False

        
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame and isRightSame