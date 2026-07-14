"""
Optimize

also use backtracking however there are duplicate so we need to sort the array and skip the element if we traverse before

Time:
if there is no duplicate O(N * 2^N), sort is O(NlogN) which is less than O(N* 2^N)

Space:
auxiliary space: stack + sort + path = O(N)
output + auxiliary space: path + all node + auxiliary space = O(N * 2^N)
"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()                 # time: O(NlogN), space: O(N)
        def backtracking(start, path):
            ans.append(path[:])     # can not add `return` in here, or else first loop in in will terminate the function
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        backtracking(0, [])
        return ans