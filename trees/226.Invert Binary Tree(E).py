# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
Optimize

use dfs to recursively invert the node

Time:
O(N)

Space:
recursion call stack
O(H), H is tree height, worst O(N), avg O(logN)

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Preorder (Top-down)
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
"""
BFS (Iterative + Queue)
"""    
from collections import deque                                                                                 
class Solution:                                                                                               
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:                                     
        if not root:                                                                                          
            return None                                                                                       
                                                                                                            
        # 1. 初始化 Queue，把起點 (root) 放進去                                                               
        queue = deque([root])                                                                                 
                                                                                                            
        # 2. 只要隊列裡面還有節點，就繼續處理                                                                 
        while queue:                                                                                          
            # 取出最前面的一個節點                                                                            
            curr = queue.popleft()                                                                            
                                                                                                            
            # 3. 本層邏輯：交換當前節點的左右子樹                                                             
            curr.left, curr.right = curr.right, curr.left                                                     
                                                                                                        
            # 4. 把小孩加入隊列，等待之後處理                                                                 
            if curr.left:                                                                                     
                queue.append(curr.left)                                                                       
            if curr.right:                                                                                    
                queue.append(curr.right)                                                                      
                                                                                                            
        # 最後回傳原本的 root，此時整棵樹已經被翻轉完了                                                       
        return root