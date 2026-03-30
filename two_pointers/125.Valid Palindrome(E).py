"""
My Solution

preprocess the string(Ex: change to lowercase and remove space)
use two pointer, one from begin another from the end, compare each char till they meat in the middle

Time:
O(N), because we need to iterate first for preprocess

Space:
O(N)
"""
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         string = "".join(c.lower() for c in s if c.isalnum())
#         left = 0
#         right = len(string) - 1
#         while(left < right):
#             if (string[left] != string[right]):
#                 return False
#             left += 1
#             right -= 1
#         return True

"""
Optimize

use original stringn to do the logic

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right: left += 1
            while not s[right].isalnum() and left < right: right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True


