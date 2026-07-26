from typing import List
"""
My Solution

in order to find all the permutations we need to use backtracking
since the order matters in permutations, ex: 1,2,3 is different than 2,1,3
so we can not use the index to iterate the list, cause that will prevent us to look backward
in every path we need to know which element is used, and pick the element that is not used yet
and add the result to the ans when the length match len(nums)

ex: 1,2,3
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

[]->[1]->[1,2]->[1,2,3]
         [1,3]->[1,3,2]
    [2]->[2,1]->[2,1,3]    

Time:
O(N! * N), N! for total node(leaves) level1, 2, 3... is far less node than last level, N for copy path[:]

Space:
auxiliary space: O(N) for path, O(N) for stack (tree depth), O(N) for used -> O(N)
auxiliary space + output space: O(N) + O(N! * N), there are N! node and each node cost length N
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        ans = []
        def backtracking(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for num in nums:
                if num not in used:
                    path.append(num)
                    used.add(num)
                    backtracking(path)
                    path.pop()
                    used.remove(num)
        backtracking([])
        return ans