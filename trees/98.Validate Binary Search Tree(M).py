# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
My Solution

use dfs top down to check if every node meets the requirements(left.val < node.val < right.val)

ex:
[]
[1]

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, left_val, right_val):
            if not root: return True
            if not (left_val < root.val < right_val): return False

            return valid(root.left, left_val, root.val) and valid(root.right, root.val, right_val)
        return valid(root, float('-inf'), float('inf'))

"""
Iterative in-order traversal, use iterative can stop early

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrderTraversal(root):
            st, val, cur = [], float('-inf'), root
            while st or cur:
                while cur:
                    st.append(cur)
                    cur = cur.left
                cur = st.pop()
                if cur.val <= val: return False
                val = cur.val
                cur = cur.right
            return True
        return inOrderTraversal(root)