"""
My Solution

use a hash map to store the num and the current longest length while iterating the nums
after storing to the map, use while loop to check if num+1 exist in the map 
ex:
[100,4,200,1,3,2]
map: 
100,1
4, 1
200, 1
1, 4
3, 2
2, 3

be careful of [], [1], [1, 1]

Time:
O(N)

Space:
O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                length = 0
                while num in num_set:
                    length += 1
                    num += 1
                ans = max(ans, length)
        return ans