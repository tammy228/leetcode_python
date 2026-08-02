"""
My Solution(WA)(although heapq can find min. but the list is not sorted)

in order to streaming add the element, we can use heap to store the timeslot
every new book time, we can use binary search to find if there is overlap
"""
import heapq
class MyCalendar:

    def __init__(self):
        self.heap = []

    def isOverlapped(self, time: tuple):
        i = 0
        # left side no overlap
        while i < len(self.heap) and self.heap[i][1] <= time[0]:
            i += 1

        if i != len(self.heap):
            return True if time[1] > self.heap[i][0] else False

        return False

        
    def book(self, startTime: int, endTime: int) -> bool:
        if self.isOverlapped((startTime, endTime)):
           return False
        heapq.heappush(self.heap, (startTime, endTime))
        return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

"""
Optimize

use list and binary search to find the first start >= startTime
"""
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        left, right = 0, len(self.booked)
        # binary search to find first start >= startTime
        # right will be the first start >= startTime index
        while left < right:
            mid = (left + right) // 2
            if self.booked[mid][0] < startTime:
                left = mid + 1
            else:
                right = mid

        idx = right
        # check idx-1 element if overlapped
        if idx > 0 and self.booked[idx-1][1] > startTime:
            return False

        # check idx element if overlapped
        if idx < len(self.booked) and self.booked[idx][0] <= endTime and startTime <= self.booked[idx][1]:
            return False


        self.booked.insert(idx, (startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)