from typing import List
"""
Optimize

check
is edges directional
cycle in edges?

Tree definition
connected and no cycle

a valid tree requires n-1 edegs(check if connected),
check the number of edges first then use union find to check if there is cycle

ex:
n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
n=3, edges=[[0,1],[1,2],[0,2]]

Time:
union O(1)
find  O(1)
total: O(E)

Space:
O(N) for parent[] and size[]
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            
            # small tree under big tree, ra = small, rb = big
            if size[ra] > size[rb]:
                ra, rb = rb, ra

            parent[ra] = rb
            size[rb] += size[ra]
            return True

        for a, b in edges:
            if not union(a, b):
                return False
        return True
"""
Opitimize 2

bfs/dfs can also check connectivity, if traverse n nodes means they are connected

check if there is n-1 edges(check if cycle),

Time:
O(V + E), V = N, E = N-1, therefore O(N)

Space
O(V + E) = O(N)


"""
from collections import defaultdict, deque
def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)          # 無向要雙向

    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == n