# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
"""
Optimize

same as 105., but postorder need to start with end

Time:
O(N)

Space:
O(N), for in_index, O(H) for stack 
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and postorder: return None
        vals = iter(reversed(postorder))
        in_index = {value: i for i, value in enumerate(inorder)}
        def dfs(left, right):
            if left > right: return None
            val = next(vals)
            node = TreeNode(val)
            mid_index = in_index[val]
            node.right = dfs(mid_index + 1, right)
            node.left = dfs(left, mid_index - 1)

            return node
        return dfs(0, len(inorder) - 1)