# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
"""
My Solution
since linked list can't iterate in reverse order. we need to find total_length and remove (total_length - n)th node
how to remove:
set (total_length - n - 1)th_node.next to (total_length - n + 1)
if first node need to remove:
    head = head.next
if last node need to remove:
    set (last - 1)th_node.next = None
* need to make sure n <= total_length
* need to make sure (total_length - n - 1), (total_length - n + 1) exist

Edge
[1]

Time:
O(N)

Space:
O(1)

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        dummy = head
        if n == length:
            return head.next
        for i in range(length-n):
            if i == length - n - 1: 
                if n == 1:
                    dummy.next = None
                else:
                    dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head

"""
Optimize
use fast/slow pointer, make slow and fast pointer distance to n
if fast reach to None means slow is pointing at delete node
then we can use prev to delete the node

Time:
O(N)

Space:
O(1)
"""
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        # move fast pointer n steps first
        for _ in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        # need to return dummy.next not head, because if delete node is first one, head will still point to first node
        return dummy.next
        
  
        
