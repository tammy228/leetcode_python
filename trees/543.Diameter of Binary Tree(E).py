class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
Optimize

diameter can be calculated by using dfs, bascially diameter = max(left_child_height, right_child_height) + 1, however the problem wants diameter not height
Therefore, we need to maintain a global number that can keep track of the diameter

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        # return node height
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0

            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            self.ans = max(self.ans, left_height + right_height)

            return max(left_height, right_height) + 1
        dfs(root)
        return self.ans
        
