# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
from typing import Optional
"""
Optimize

deep copy itself is not hard, however there is random pointer in the node.
Therefore, we need two passes(iterate) and hash map to do do the algo.
first pass: create node and create old_to_new_map dict
second pass: while link all the node we can use the dict to set the random pointer

Edge
[]

Time:
O(N)

Space:
O(N)
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # add None: None can avoid if the node is None will accur error
        old_to_new_node = {None: None}
        cur = head
        while cur:
            new = Node(cur.val)
            old_to_new_node[cur] = new
            cur = cur.next
        
        cur = head
        while cur:
            new = old_to_new_node[cur]
            new.next = old_to_new_node[cur.next]
            new.random = old_to_new_node[cur.random]
            cur = cur.next
        
        return old_to_new_node[head]
