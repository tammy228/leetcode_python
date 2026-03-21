from typing import List

"""
My Solution

While iterating the list, use dictionary to keep track of the difference and the index,
and if met the key then there is solution

Time:
O(N)

Space:
O(N), where N is len(target)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for id, num in enumerate(nums):
            if num in dict_num:
                return [id, dict_num[num]]
            else:
                dict_num[target - num] = id
        return []