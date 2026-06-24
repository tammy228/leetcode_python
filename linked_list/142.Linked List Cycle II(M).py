# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
"""
Optimize

Two pointer

head-cycle_start: L
cycle total length: C
cycle_start-meeting_point: X
meeting_point-cycle_start: Y
C = X + Y, if slow distance is L + X, then fast dis. will be 2(L + X)(because V_fast = 2*V_slow)
2(L + X) = L + X + nC -> 2L + 2X = L + X + nX + nY -> L = (n - 1)X + nY -> L = nC - X -> L = (n - 1)C + Y
which means if we set a pointer at head and move slow pointer and head pointer at the same time
cycle_start = head pointer and slow pointer meeting point

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None