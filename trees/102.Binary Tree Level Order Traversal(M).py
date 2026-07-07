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

use deque to impl. queue for bfs

ex:
[]
[1]
[3,9,20,null,null,15,7]

Time:
O(N)

Space:
O(W), max width of the tree, in perfect binary tree, last level leaf node will be N/2, therefor worst will be O(N)
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q, ans = deque([root]), []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(level)
        return ans