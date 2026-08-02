from typing import List
"""
My Solution(WA)
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for start, end in intervals:
            if newInterval[0] > end:
                ans.append([start, end])
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
                if newInterval[1] == end:
                    ans.append(newInterval)
                    newInterval[0] = float('inf')
        if newInterval[0] != float('inf'):
            ans.append(newInterval)
        return ans
"""
Optimize

divided insert to three parts

Time:
O(N)

Space:
output space: O(N)
"""
def insert(intervals, newInterval):
    res = []
    i, n = 0, len(intervals)
    new_start, new_end = newInterval

    # 階段 1:結束早於 new 起點 → 在 new 左邊,沒重疊
    while i < n and intervals[i][1] < new_start:
        res.append(intervals[i])
        i += 1

    # 階段 2:有重疊的全部吸收,擴張 new 的邊界
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end   = max(new_end,   intervals[i][1])
        i += 1
    res.append([new_start, new_end])

    # 階段 3:剩下的都在 new 右邊,直接接上
    while i < n:
        res.append(intervals[i])
        i += 1

    return res