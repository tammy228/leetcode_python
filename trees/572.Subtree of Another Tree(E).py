# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
use dfs to iterate all node in root, and compare each node with subRoot

Time:
O(N*M)

Space:
O(H), worst O(N), N is root all node(not subroot because subroot comparison is called by root), avg O(logN)
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
        if not root and subRoot:
            return False

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)