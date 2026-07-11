# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
My Solution

if the tree is bst, we can use the val to determine which side to go

Time:
worst O(N), avg O(logN)

Space:
O(1)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val: cur = cur.left
            elif p.val > cur.val and q.val > cur.val: cur = cur.right
            else:
                return cur
        return None