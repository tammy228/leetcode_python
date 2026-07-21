"""
My Solution

use dp as 5. and check each palindrome substring and push into set 

ex:
[]
[1]

Time:
O(N^2)

Space:
O(1)

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.ans += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return self.ans