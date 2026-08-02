"""
My Solution

due to the destination(from, to) <= 1000, therefore just create a 1k array to record all the passengers
is more fatster than seperate all the from , to event then sort

1. create 1000 length array
2. init the passenger to array
2.a from-> ex:2 people in 3,  arr[3] = 2
2.b to  -> ex:2 people in 4,  arr[4] = -2
3. iterate the array and accumulate the passenger, while accumulating check if passenger over capacity

Time:
O(N), N for len(trips)

Space:
O(1000) == O(1)
"""
from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1001
        max_pass = 0
        for num, start, end in trips:
            locations[start] += num
            locations[end] += -num

        for i in range(1000):
            max_pass += locations[i]
            if max_pass > capacity:
                return False
        return True