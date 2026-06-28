"""
Optimize

use double linked list and hash map to create LRU cache, because we need to update recent used key we need double linked list

double linked list:
** 
we need to use dummy node to maintain double linked list, because if remove/insert is in first/last node 
it will be complicated
**

least |  left <-> [1,1] <-> [2,2] <-> right  | most recent


put:
1. check if over capacity
if over capacity:
    pop the least node, remove from hash map
2. add it to list and hash map

get:
1. go to hash map for value
2. update linked list
"""
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: int, node}

        # init left, right node for double linked list
        # left = least recent used
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    # remove node from list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # insert node to right
    def insert(self, node): 
        node.next = self.right
        node.prev = self.right.prev
        node.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # update linked list
            # need to remove first then insert, because when you insert, it's in last place, then remove
            # basically you did not add any node
            cur = self.cache[key]
            self.remove(cur)
            self.insert(cur)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # we don't need the old node
        if key in self.cache:
            self.remove(self.cache[key])
        
        # create node and insert to list
        cur = Node(key, value)
        self.cache[key] = cur
        self.insert(cur)

        # check if over capacity
        if len(self.cache) > self.capacity:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)
