from typing import List
"""
My Solution

check
is len(input) >= 2?

In order to know the top floor cost, we can start from stair 0 or 1, we can use a dp array to record what is the min. cost on dp[i]
for dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
for the base case
dp[0] = dp[1] = 0

Time:
O(N)

Space:
O(N)

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        
        return dp[len(cost)]
    
"""
Optimize

instead of creating intire array we can maintain only two var.

Time:
O(N)

Space:
O(1)
"""
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2: return 0
        prev2 = 0
        prev1 = 0
        for i in range(2, len(cost)+1):
            result = min(prev2+cost[i-2], prev1+cost[i-1])
            prev2 = prev1
            prev1 = result

        return prev1