# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
"""
Optimize

1. the first node of the preorder must be the root
2. use the root to find the position in inorder, left portion must be left subtree, right portion will be right subtree
2.b after we find the position, we need to tell dfs the start and end index(using index instead of slicing the list reduce the memory usage)
3. recursively call and build the tree
ex:
pre: 1-2-3
in: 2-1-3
in_index = {
    2:0,
    1:1,
    3,2
}
dry run:
dfs(0, 2)
    node: 1
    mid: 1
    pre_index = [1]
dfs(0, 0)
    node: 2
    mid: 0
    pre_index = [2]
dfs(0, -1)
    none
len(pre) != len(in)
pre:[]
in: []

Time:
O(N)

Space:
stack O(H), worst O(N), avg O(logN), O(N) for in_index
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return None
        pre_index = [0] # use list to go through preorder list., can change to iter()
        in_index = {value : i for i, value in enumerate(inorder)}
        def dfs(left, right):
            if left > right: return None
            node = TreeNode(preorder[pre_index[0]])
            mid_index = in_index[preorder[pre_index[0]]]
            pre_index[0] += 1
            node.left = dfs(left, mid_index - 1)
            node.right = dfs(mid_index + 1, right)

            return node
        return dfs(0, len(inorder) - 1)
