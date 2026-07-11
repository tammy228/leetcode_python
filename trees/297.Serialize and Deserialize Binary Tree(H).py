# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Optimize

serialize the tree into preorder
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node: res.append("N"); return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        vals = iter(data)

        def dfs():
            val = next(vals)
            if val == "N": return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
"""
BFS
"""
from collections import deque
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        return ",".join(res)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 1 and data[0] == "N": return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1
        while queue:
            cur = queue.popleft()

            if data[index] != "N":
                cur.left = TreeNode(int(data[index]))
                queue.append(cur.left)
            
            index += 1
            if data[index] != "N":
                cur.right = TreeNode(int(data[index]))
                queue.append(cur.right)
            
            index += 1

        return root