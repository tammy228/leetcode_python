"""
My Solution

check
[]

sort with start, for each interval we compare if inter[i+1].start < inter[i].end
if yes: then merge the interval
if no: push to ans

Time:
O(NlogN)

Space:
auxiliary space: sort + intervals[1:] = O(N)
output space: O(N)
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
        return ans