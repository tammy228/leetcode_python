"""
My Solution

check
negative value
maximum length
[]
[1]

since the question ask for two biggest number, if we sort with each round, the tc. will be very bad
therefore we can use heap to found two biggest number, for each round we insert the number it's only gonna take O(logN)

Time:
init + while = O(N) + O(NlogN) = O(NlogN)

Space:
auxiliary space = O(N)
"""
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        heap = [-s for s in stones]
        # init heap(max heap)
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x < y:
                val = y - x
                heapq.heappush(heap, val)
        return heap[0] if len(heap) > 1 else 0