"""
My Solution

check
[]
start < end
if [1,3][3,5] overlapped?

in order to keep the most intervals, we want to keep the smaller end as possible
1. sort the interval with end
2. iterate the intervals, if overlapped ans++, otherwise keep the interval

Time:
O(NlogN)

Space:
O(N) for sorting
"""
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        ans = 0
        prev_end = float('-inf')
        intervals.sort(key=lambda x: x[1])

        for start, end in intervals:
            if start < prev_end:
                ans += 1
            else:
                prev_end = end
        return ans
