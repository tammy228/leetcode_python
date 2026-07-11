# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
"""
Optimize

unlike inorder, postorder and preorder can not use root node to divide the list
inorder = [ (左子樹所有點), Root, (右子樹所有點) ]
Preorder:  [ Root, (左子樹所有點), (右子樹所有點) ]                                                                      │
Postorder: [ (左子樹所有點), (右子樹所有點), Root ]

Ex:
preorder: [1, 2, 4, 5, 3]
postorder: [4, 5, 2, 3, 1]
if use node(1), we don't know [4,5,2,3] which nodes are left subtree, 
Therefore, we need to use the first node in left subtree(assumed the next node of root must be left subtree)

Time:
O(N)

Space:
O(N), for pos_index, O(H) for stack
"""
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos_index = {value: i for i, value in enumerate(postorder)}
        self.pre_index = 0
        def dfs(post_left, post_right):
            if post_left > post_right: return None
            val = preorder[self.pre_index]
            self.pre_index += 1
            node = TreeNode(val)

            # need to early return if the node is leaf, or else pos_index[left_root_val] will error
            if post_left == post_right:
                return node

            # use first node of left subtree to do slicing
            left_root_val = preorder[self.pre_index]
            mid_index = pos_index[left_root_val]
            node.left = dfs(post_left, mid_index)
            node.right = dfs(mid_index + 1, post_right - 1)     # be carful for 'post_right - 1', post_right it self is root node

            return node
        return dfs(0, len(postorder) - 1)
