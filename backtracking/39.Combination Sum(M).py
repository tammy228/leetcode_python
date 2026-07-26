"""
Optimize

no duplicate number, same as subset use backtracking to find target number


"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtracking(start, path, remain): # sum(path) is expensive, we can keep track of remaining
            if remain == 0:
                ans.append(path[:])
                # because candidats[i] > 2, if already remain == 0 we don't need check the child, 
                # it will only break in `if remain - candidate[i] < 0`
                return                         
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtracking(i, path, remain - candidates[i])
                path.pop()
        backtracking(0, [], target)
        return ans

"""
Optimize2

add sort candidate, and change the condition block from return to break
because if this node can not match, the nodes come after definitely can not match

Time(total node):
branch: N choice
max depth: worst is T/M, T for target, M for minimum number
path: worst need T/M time to copy
sort: O(NlogN)

O(N^(T/M) + NlogN) (len(level)^depth)

Space:
auxiliary space: sort + path + stack = O(N) + worst O(N) + O(T/M) = O(N + T/M)
output + auxiliary = O(S*(T/M) + N + T/M), S for len(ans), every each answer length will be T/M
"""
from typing import List
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtracking(start, path, remain): # sum(path) is expensive, we can keep track of remaining
            if remain == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                if remain < 0:
                    break
                path.append(candidates[i])
                backtracking(i, path, remain - candidates[i])
                path.pop()
        backtracking(0, [], target)
        return ans