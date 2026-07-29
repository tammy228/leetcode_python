"""
My Solution

same as subsets, we can see this problem as where to put the dot. the time to collect the answer is when
len(path) == 4 and also there is no number left in the string

because len(path) >= 4 break, the tree won't be too deep
for branch, the maximum len(char) we can pick is 3 char
therefore, the total treenode is 3^1+3^2+3^3+3^4

Time:
O(3^M), M is depth which maximum is 4

Space:
auxiliary space: stack, path = O(4)+O(4) = O(1)
output + auxiliary = O(1)(3^4, each segment only 3 choice, each combination maximum length is 12 + 3 dot) + O(1)
"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtracking(start, path):
            if len(path) == 4 and start == len(s):
                ans.append(".".join(path[:]))
                return
            for i in range(start, len(s)):
                st = s[start:i+1]
                if (s[start] == "0" and len(st) > 1) or int(st) > 255:
                    continue
                if len(path) >= 4:
                    break
                path.append(st)
                backtracking(i+1, path)
                path.pop()
        backtracking(0, [])
        return ans 