"""
Optimize

also use backtracking to find all the conbinations

ex: [10,1,2,7,6,1,5], target = 8

Time:
sort: O(NlogN)
total: O(N*2^N), N for path[:] total 2^N node

Space:
auxiliary space: sort + path + stack = O(N) + O(N) + worst O(N) = O(N)
output + auxiliary space: worst O(2^N * N) + O(N) = O(2^N * N)

"""
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()                       # sort candidate because we need to know if there is duplicate, and also for early stopping
        def backtracking(start, path, remain):
            if remain == 0:
                ans.append(path[:])
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue                    # can not use return, or else it will miss the number behind
                if remain - candidates[i] < 0:
                    break
                path.append(candidates[i])
                backtracking(i+1, path, remain - candidates[i]) # use i+1 to make sure every number is used once
                path.pop()
        backtracking(0, [], target)
        return ans
