from typing import List
"""
My Solution

check
negative number
how big is the number
minimum len(nums)?

we can use dp array to keep track of the maximum amount in ith house, for dp[i] i have two choices
1. rob i-1th and pass the ith house
2. rob i-2th and ith house
=> dp[i] = max(dp[i-1], dp[i-2]+nums[i])

ex:
[1,2,3,1], ans = 4
[1]
[1,3]

Time:
O(N)

Space:
O(N)

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[len(nums)-1]

"""
Optimize

Time:
O(N)

Space:
O(1)
""" 
class Solution2:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for num in nums:
            result = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = result

        return prev1