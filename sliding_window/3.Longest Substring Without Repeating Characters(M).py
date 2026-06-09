"""
My Solution

use sliding window to track current char set, if encountered same char on right pointer
we remove the char from left until the same char is removed from the set

Time:
O(N)

Space:
O(N)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_chars = set()
        left, right = 0, 0
        ans = 0
        # for loop is faster than while loop, this is and standard knowledge...
        #while right < len(s):
        for right in range(len(s)):
            while s[right] in visited_chars:
                visited_chars.remove(s[left])
                left += 1
            visited_chars.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
"""
Optimize

use hash map to record the last index of the char, we can jump to index instead of using while

Time:
O(N)

Space
O(N)
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        last_seen = defaultdict(int)
        for right in range(len(s)):
            # because we directly jump to the index, we did not remove the info from left->last_seen[s[right]] + 1
            # therefore, we need to prevent left pointer jump back
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1
            last_seen[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans