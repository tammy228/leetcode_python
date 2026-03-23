from typing import List
from collections import defaultdict
"""
My Solution

Use dictionary to record the times of each num and find the top k elements

Time:
O(N + k * M)

Space:
O(N)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map = {}
        ans = []
        for num in nums:
            dict_map[num] = dict_map.get(num, 0) + 1

        for _ in range(k):
            max_key = max(dict_map, key=dict_map.get)
            ans.append(max_key)
            dict_map[max_key] = -1

        return ans
            
"""
Optimize

using bucket sort

Time:
O(N)

Space:
O(N)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map = {}
        ans = []
        freq_bucket = [[] for i in range(len(nums) + 1)]
        for num in nums:
            dict_map[num] = dict_map.get(num, 0) + 1

        for key, value in dict_map.items():
            freq_bucket[value].append(key)

        for i in range(len(freq_bucket) - 1, 0, -1):
            for m in freq_bucket[i]:
                if len(ans) == k:
                    return ans
                ans.append(m)
        return ans
        
        