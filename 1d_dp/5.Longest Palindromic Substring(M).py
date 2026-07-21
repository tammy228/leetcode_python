"""
Optimize

check
upperletter and lowerletter
punctuation

in order to find all possible combination, we need to find all substring that match palindrome
for each index we need to check odd and even number of string and find the longest palindrome
for finding longest palindrome
we can start from the center and expand to both side, ex: if s[1..r] is palindrome, and s[l-1] == s[r+1], then s[l-1...r+1] is palindrome

ex:
babad

Time:
O(N^2)

Space:
O(N), worst case each index slice copy N times, not O(N^2) in any time there will only be odd_result, even_result, ans.
If we create a 2d array then it will be O(1)


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r] # include l+1 not include r
        for i in range(len(s)):
            odd_result = expand(i, i)
            even_result = expand(i, i+1)
            if len(odd_result) > len(ans):
                ans = odd_result
            if len(even_result) > len(ans):
                ans = even_result
        return ans