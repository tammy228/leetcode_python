# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
My Solution

due to early return we can use iterative traversal to count k element and return the value

ex:
[]
k > n?

Time:
O(N)

Space:
O(H), worst O(N), avg O(logN)
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st, cur = [], root
        while st or cur:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            k -= 1
            if k == 0: return cur.val
            cur = cur.right
        return 0