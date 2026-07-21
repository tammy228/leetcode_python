from typing import List
"""
Optimize

since the house is circular, we can either stole first or last house, so we divide into two problems
1. stole first = remove last house = nums[:-1]
2. stole last = remove first house = nums[1:]
ans = max(1, 2)

Time:
O(N)

Space:
O(N), for slicing will duplicate another array

ex:
[1]
[1,2]
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # 1.
        prev1_first, prev2_first = 0, 0
        for num in nums[:-1]:
            result = max(prev1_first, prev2_first+num)
            prev2_first = prev1_first
            prev1_first = result
        
        # 2.
        prev1_last, prev2_last = 0, 0
        for num in nums[1:]:
            result = max(prev1_last, prev2_last+num)
            prev2_last = prev1_last
            prev1_last = result
        
        return max(prev1_last, prev1_first)

"""
Optimize

use helper function to reduce repeated for loop
"""
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def helper(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                result = max(prev1, prev2+num)
                prev2 = prev1
                prev1 = result
            return prev1
        return max(helper(nums[:-1]), helper(nums[1:]))
