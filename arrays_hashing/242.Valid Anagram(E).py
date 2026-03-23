
"""
My Solution

Use dictionary to track both string and compare the dictionary

Time:
O(N)

Space:
O(26 * 2) = O(1)

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_t, dict_s = {}, {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1

            if t[i] not in dict_t:
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1
        return dict_s == dict_t
    
"""
Optimize

More pythonic writing for same idea
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_char =  {}
        for i in range(len(s)):
            dict_char[s[i]] = dict_char.get(s[i], 0) + 1
            dict_char[t[i]] = dict_char.get(t[i], 0) - 1
        for val in dict_char.values():
            if val != 0:
                return False
        return True

    