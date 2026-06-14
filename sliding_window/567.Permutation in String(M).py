"""
My Solution

use a dictionary to record s1, and using sliding window which size is len(s1) to check s2
return false if len(s2) < len(s1)

Time:
O(M)

Space:
O(N*M)
"""
# from collections import defaultdict
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1_chars = defaultdict(int)
#         temp_chars = defaultdict(int)
#         # i nit s1
#         for char in s1:
#             s1_chars[char] += 1

#         for i in range(len(s2)):
#             if i < len(s1):
#                 temp_chars[s2[i]] += 1
#             else:
#                 temp_chars[s2[i - len(s1)]] -= 1
#                 if temp_chars[s2[i - len(s1)]] == 0:
#                     del temp_chars[s2[i - len(s1)]]
#                 temp_chars[s2[i]] += 1
#             if s1_chars == temp_chars:
#                     return True
#         return False

"""
Optimize

Use a variable to track the status of sliding windows, therefore we don't need to compare dict everytime

Time:
O(M)

Space:
O(26)

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        matches = 0
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            left_idx = ord(s2[i - len(s1)]) - ord('a')
            s2_count[left_idx] -= 1
            if s1_count[left_idx] == s2_count[left_idx]:
                matches += 1
            elif s1_count[left_idx] == s2_count[left_idx] + 1:
                matches -= 1
            
            right_idx = ord(s2[i]) - ord('a')
            s2_count[right_idx] += 1
            if s1_count[right_idx] == s2_count[right_idx]:
                matches += 1
            elif s1_count[right_idx] == s2_count[right_idx] - 1:
                matches -= 1
        # be careful of the last change
        return matches == 26
            