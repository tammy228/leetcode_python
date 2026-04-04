"""
My Solution

use stack to keep track of the paratheses status,
if open parentheses : push to stack
close parentheses: pop and check if it's corresponding one

Time:
O(N)

Space:
O(N)
"""
class Solution:
    
    def isValid(self, s: str) -> bool:
        para_dict = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        if len(s) % 2 != 0: return False

        st = []
        for para in s:
            if para in para_dict:
                open_pair = para_dict[para]
                if not st or st[-1] != open_pair:
                    return False
                st.pop() 
            else:
                st.append(para)
        return not st

        