# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
"""
My Solution

find the middle item and iterate the first half
while iterating insert second half item to first half

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        tail = slow
        prev = None
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
            
        dummy = head
        while prev.next:
            temp1 = dummy.next
            dummy.next = prev
            temp2 = prev.next
            prev.next = temp1
            prev = temp2
            dummy = temp1
