from typing import List
from collections import defaultdict, deque
"""
My Solution

same as Course Schedule, use Kahn's algo
1. init adj./ind. list for all Courses
2. put ind[i] == 0 into queue
3. while queue is not empty
3.a pop the course and push into order
3.b visit the neighbors of the course and update the ind. list
3.c push ind[i] == 0 into queue
4. check if there is cycle, if cycle return -1, else return order

check
will there be double pair
slef-cycle?
[]
if there is cycle what should we return

Time:
O(V+E)

Space:
O(V+E)
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        ind = [0] * numCourses
        q = deque()
        adj = defaultdict(list)
        for a, b in prerequisites:   # b -> a
            adj[b].append(a)
            ind[a] += 1

        for index, indegree in enumerate(ind):
            if indegree == 0:
                q.append(index)
        
        while q:
            course = q.popleft()
            ans.append(course)
            for nei in adj[course]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        
        return ans if len(ans) == numCourses else []