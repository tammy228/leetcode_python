"""
Recursion(TLE)

Time:


"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

"""
Memoization

Time:
O(N)

Space:
O(N), for memo
"""
class Solution2:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = climb(i-1) + climb(i-2)
            return memo[i]
        return climb(n)
    
"""
Tabluation

Time:
O(N)

Space:
O(N), for dp[]
"""
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1) # dp[i] = how many ways to reach level i
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]