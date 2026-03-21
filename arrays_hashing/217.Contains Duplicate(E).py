
from typing import List

"""
My Solution

using set to record the elements in list and use set as data structure
return true as soon as the loop met the same element

Time:
O(N)

Space:
O(N)
"""
def hasDuplicate(self, nums: List[int]) -> bool:
    container = set()
    for num in nums:
        if num in container:
            return True
        else:
            container.add(num)
    return False