"""
My Solution

1. use siding window to first find the valid window
2. shift the window until found the next valid window
3. check if left pointer can move right to get minimum window

s = "a", t = "a"
s = "ADOBECODEBANC", t = "ABC"

WA
"""
from collections import defaultdict
# class Solution:
#     def check_dict(self, freq_t, freq_window):
#         for key, value in freq_t.items():
#             if freq_window[key] < value:
#                 return False

#         return True
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s) : return ""
#         freq_t = defaultdict(int)
#         freq_window = defaultdict(int)
#         left, right = 0, 0
#         for ch in t:
#             freq_t[ch] += 1
        
#         # case s="a", t="b" will be wrong, there is no matches in s, but still assign idx to right
#         # 1.
#         is_checked = False
#         for idx in range(len(s)):
#             freq_window[s[idx]] += 1
#             if self.check_dict(freq_t, freq_window):
#                 is_checked = True
#                 break
        
#         if not is_checked and idx == len(s) - 1: return ""
#         ans = s[0:idx+1]
#         right = idx
#         # 2. 3.
#         for right in range(idx+1, len(s)):
#             freq_window[s[right]] += 1
#             freq_window[s[left]] -= 1
#             left += 1
#             while self.check_dict(freq_t, freq_window):
#                 freq_window[s[left]] -= 1
#                 left += 1

#         ans = s[left-1:right+1] 
#         return ans

"""
Optimize

don't need to get the first window, loop below steps
1. extend right pointer until freq_window meet freq_t
2. update length and the substring
3. keep shifting left pointer until freq_window don't meet freq_t 

compare freq_window and freq_t
** compare whole dictionary is expensive **
use variable to record the change

s "aa" t "aa"
s="z", t="a"
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_window = defaultdict(int)
        freq_t = defaultdict(int)
        left = 0
        min_length = float('inf')
        ans = ""
        for ch in t:
            freq_t[ch] += 1
        have, need = 0, len(freq_t)

        # 1.
        for right in range(len(s)):
            if s[right] in freq_t:
                freq_window[s[right]] += 1
                if freq_window[s[right]] == freq_t[s[right]]:
                    have += 1
                # 3.
                while have >= need:
                    if right - left + 1 < min_length:
                        ans = s[left:right+1]
                        min_length = right - left + 1
                    if s[left] in freq_t:
                        freq_window[s[left]] -= 1
                        if freq_window[s[left]] < freq_t[s[left]]:
                            have -= 1
                    left += 1
        return ans