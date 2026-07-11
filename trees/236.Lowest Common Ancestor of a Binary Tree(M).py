# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
My Solution

because this is a normal binary tree, we can not mode the cur pointer by cur value
we can use dfs(bottom-up) to see find lca

ex:
p or q not in tree
Time:
O(H), worst O(N), O(logN)

Space:
O(H), wosrt O(N), O(logN)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q: return root

        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)

        if L and R: return root
        return L or R