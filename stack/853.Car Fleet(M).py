"""
My Solution

In order to track the car fleet, we can draw the number line to visualize the process
from the drawing we can know, if the arrival time from left position is smaller than the time on the right
they will become car fleet.
1. caculate all position arrival time
2. sort the arrival time according to the position
3. iterate the arrival time, if the time is bigger than the stack top than pop it out
4. return len(stack)

Time:
O(NlogN)

Space:
O(N)

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        pos_times = []
        for pos, sp in zip(position, speed):
            pos_times.append((pos, (target - pos) / sp))
        
        pos_times.sort()

        for pos_time in pos_times:
            time = pos_time[1]
            while(st and st[-1] <= time):
                st.pop()
            if not st or st[-1] > time:
                st.append(time)
            
        return len(st)

"""
Optimize

iterate pos_times backward for more straight forward method
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        pos_times = []
        for pos, sp in zip(position, speed):
            pos_times.append((pos, (target - pos) / sp))
        
        pos_times.sort(reverse=True)

        for pos_time in pos_times:
            if not st or pos_time[1] > st[-1]:
                st.append(pos_time[1])
            
        return len(st)

"""
Optimize 2

1. Use list comprehension instead of .append
2. sort(), use key lambda to reduce unnecessary comparsion/preparation
* above method is comparing tuple, but we just need int
3. use unpacking instead of index accessing
* `for p, s in pairs:` is faster than pairs[1]

Time:
O(NlogN)

Space:
O(N)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        pos_sps = [(pos, sp) for pos, sp in zip(position, speed)]
        pos_sps.sort(key=lambda x: x[0], reverse=True)

        last_time = 0
        for p, s in pos_sps:
            time = float((target - p) / s)
            if time > last_time:
                ans += 1
                last_time = time
        return ans