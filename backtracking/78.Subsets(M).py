"""
Optimize

for all possibilities we need to use backtracking to find all subsets

Time;
O(N * 2^N), there are 2^N nodes for all subsets, and for path[:] is O(N)

Space:
no output space, just stack and path[:]: O(log 2^N) = O(2N) = O(N)
paht[:] + ans : O(N + 2^N * N) = O(2^N * N)
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(start, path):
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        backtracking(0, [])
        return ans