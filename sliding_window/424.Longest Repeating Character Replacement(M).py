from collections import defaultdict
"""
Optimize

while using sliding window to iterate the string, we also need to use dict. to track the freq. of the char.
keep moving right pointer to find longest substring while the length - max_freq(char) <= k
else moving left pointer until the window is valid

Time:
O(N)

Space:
O(26) = O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_char = defaultdict(int)
        left = 0
        max_freq = 0
        ans = 0
        for right in range(len(s)):
            freq_char[s[right]] += 1
            max_freq = max(max_freq, freq_char[s[right]])
            while right - left + 1 - max_freq > k:
                # we don't need update max_freq because it's only gonna get smaller
                # and if max_freq get smaller it won't help to get longest ans
                freq_char[s[left]] -= 1
                left +=1
            ans = max(ans, right - left + 1)
        return ans

"""
Optimize 2

replacing `while` to `if`, for finding longest window, we actually only need `if` not `while`,
while loop means that the window will always be valid, however the shorter valid window does not help for the final answer
using `if` we are ensure the window is going to be the same or get bigger,
enter if condition means that current length L is not valid, we need to rollback to L-1 length no matter it is valid in current index 

Time:
O(N)

Space:
O(26) = O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_char = defaultdict(int)
        left = 0
        max_freq = 0
        ans = 0
        for right in range(len(s)):
            freq_char[s[right]] += 1
            max_freq = max(max_freq, freq_char[s[right]])
            if right - left + 1 - max_freq > k:
                # we don't need update max_freq because it's only gonna get smaller
                # and if max_freq get smaller it won't help to get longest ans
                freq_char[s[left]] -= 1
                left +=1
        if right - left + 1 > ans:
                ans = right - left + 1
        return ans