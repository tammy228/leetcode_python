"""
My Solution

the worst solution will be O(N^2) which iterate the array twice to find the max profit

Time:
O(N^2)

Space:
O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    ans = max(ans, prices[j] - prices[i])
        return ans

"""
Optimize

while iterating we can track the minimum number we iterated, then we can calculate the profit to current price

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            ans = max(ans, prices[i] - min_price)
        return ans