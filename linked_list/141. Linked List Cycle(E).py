
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
"""
Two pointers
use fast slow pointer to detect if there is cycle
fast pointer: move two node
slow pointer: move one node
if fast catch slow then there is a cycle
else if fast hit None then there is no cycle

Edge
[1]
[]

Time:
O(N)
* if there is no cycle, fast only cost O(N/2)
* if there is cycle, before cycle O(L), once slow enter cycle it will only cost O(C), and L + C = N, therefore total time will be O(N)

Space:
O(1)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # don't need to add fast.next == slow
            # Reason 1.: there might be no fast.next will cause error
            # Reason 2.: every each loop the dis. bewteen slow and fast will decrease by 1, eventually they will meet
            if fast == slow:
                return True
        return False