# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
My Solution

use bottom up child return max sum path, however maxPathSum could be in left+curr+right, therefore we need to update max_sum to global var.
but if we choose this path we can not extend the path any longer
and dfs will be return max path without spilting
ex:
[]
[1]
[-1]

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = float('-inf')

        # return path sum without spilting
        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_result = max(left, 0)
            right_result = max(right, 0)

            self.ans = max(self.ans, left_result+right_result+node.val)

            return node.val + max(left_result, right_result)
    
        dfs(root)
        return self.ans