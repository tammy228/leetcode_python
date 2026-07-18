# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
Optimize

check
is the graph connected?, will there be isolate part
directed or not directed
will there be double edges?
[]

in order to do deep copy we need to traverse the whole graph using either dfs/bfs.
however if there is cycle we can not just use dfs/bfs
we need to maintain a hashmap to record the node we traversed, if we visited the node before just return the new node
if not visited: create new node -> make copy -> go through neighbors

ex:
[[2, 3], [1, 3], [1, 2]]

Time:
O(V + E), v for all node, e for all edge

Space:
auxiliary space: stack, old_to_new = O(V) + O(V) = O(V)
auxiliary sapce + output space  = O(V) + O(V + E) = O(V + E)
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(node):
            if not node: return None
            if node in old_to_new: return old_to_new[node]
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
            