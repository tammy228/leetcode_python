from typing import List
"""
My Solution

Time:
O(NMK), N for len(s), M for len(wordset), K for substring compare

Space:
O(N+M*K), N for dp array, M for len(wordset) K for len(word)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordset = set(wordDict) # prevent duplicate

        for i in range(1, len(s) + 1):
            if dp[i-1]:
                for word in wordset:
                    if i+len(word)-1 <= len(s) and s[i-1: i+len(word)-1] == word:
                        dp[i+len(word)-1] = True
        return dp[len(s)] 

"""
Optimize

instead of searching whole dictionary we can search backwards dp[i] still be if the words before ith can be assembled
will significantly reduce the time because once we found the match we can early exit

Time:
O(N* K^2), K for max_len, normally the inner loop don't need to traverse from zero

Space
O(N + MK)
"""
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordset = set(wordDict) # prevent duplicate
        max_len = max(len(w) for w in wordset) 

        for i in range(1, len(s) + 1):
           for j in range(max(0, i-max_len), i):
               if dp[j] and s[j:i] in wordset:
                   dp[i] = True
                   break
        return dp[len(s)] 