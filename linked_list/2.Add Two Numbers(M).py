# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
"""
My Solution

1. iterate both list and concat as string, reverse the string and add them together
2. str(sum) and reverse the string and turn it to link list

ex:
l1 = [2,4,3], l2 = [5,6,4]
str1 = "243", str2 = "564"
342+465 = 807
result = "708"
7->0->8

Edge:
[], []
[], [1]

Time:
O(N + M), N = len(l1), M = len(l2)

Space:
O(N + M), string space

"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1 or not l2:
            if not l1:
                l1 = ListNode(0)
            else:
                l2 = ListNode(0)
        
        str1, str2 = "", ""
        dummy = ListNode(0)
        ans = dummy

        # 1.
        while l1:
            # string is immutable, therefor += will need to copy to new memory space, time will be O(N^2)
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        # 2.
        sum = int(str1[::-1]) + int(str2[::-1])
        result = str(sum)[::-1]
        for i in range(len(result)):
            dummy.next = ListNode(int(result[i]))
            dummy = dummy.next
        dummy.next = None

        return ans.next

"""
Optimize

Use element wise add, from ones digit, add the number, if sum over 10 then record the remainder and carry

Time:
O(N), where N = max(len(l1), len(l2))

Space:
O(1)
"""
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0

            ans_num = (l1_num + l2_num + carry) % 10
            carry = (l1_num + l2_num + carry) // 10

            dummy.next = ListNode(ans_num)
            dummy = dummy.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next
            


