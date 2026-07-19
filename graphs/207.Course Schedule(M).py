from typing import List
from collections import defaultdict, deque
"""
My Solution

check
will there be cycle prerequisites
connected or not
self-cycle?
if there is cycle, what should we return
duplicate pair, ex: [[a,b], [a,b]]

for prerequisities order we can use topology sort. for each prerequities
ex:[a,b], must take b first than a, so the graph will be that b->a, but if there is cycle we can not return any possible order
we can use bfs to do topology sort
1. we need to init the adj. list of the courses, and the indegree list of all node
2. init queue with the indegree = 0 node
3. while the queue is not None:
3.a pop the course to the answer
3.b update the indegree list, and check if there is any indegree == 0, if yes push into queue
4. check if the answer match the length of courses, if not which means there is cycle

Time:
init adj, init queue, queue = O(E) + O(V) + O(V + E) = O(V+E)

Space:
adj, queue, order = O(V + E) + O(V) + O(V) = O(V+E)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        ind = [0] * numCourses
        q = deque()
        order = []
        for ca, cb in prerequisites:  # b -> a
            adj[cb].append(ca)
            ind[ca] += 1
        
        for index, indegree in enumerate(ind):
            if indegree == 0:
                q.append(index)

        while q:
            course = q.popleft()
            order.append(course)
            for nei in adj[course]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        return len(order) == numCourses