from typing import List
"""
My Solution

due to constant space requirement, we will need to use two pointer and see array as linked list and 
use loop detection skill to find same element, and loop start point is repeated number

how to see array as linked list:
arr[i] = node(i, next= node(arr[i]))

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # index
        head = 0
        slow = nums[head]
        fast = nums[nums[head]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        
        return head