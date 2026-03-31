"""
My Solution

Use two pointer to find all trapping water area, while iterating the heights we need left and right pointers
to keep track of both side heights

Time:
O(N^2)

Space:
O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i, num in enumerate(height):
            if i == 0: continue
            left, right = i - 1, i + 1
            while left >= 0 and height[left] <= num:
                left -= 1
            while right < len(height) and height[right] <= num:
                right += 1
            ans += min(height[left], height[right]) - num

        return ans

"""
Optimize

since we need to find the minium height of both side at each position
we iterate twice, one for left side, one for right side

Time:
O(N)

Space:
O(N)

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        min_height = [0] * len(height)
        ans = 0
        # left
        max_height = 0
        for i, num in enumerate(height):
            if i > 0:
                min_height[i] = max_height 
            max_height = max(num, max_height)
        # right
        max_height = 0
        for i in reversed(range(len(height))):
            if i < len(height) - 1:
                min_height[i] = min(max_height, min_height[i])
            max_height = max(height[i], max_height)
        
        for i in range(1, len(height) - 1, 1):
            if min_height[i] > height[i]:
                ans += min_height[i]- height[i]
        
        return ans
            
"""  
Optimize 2

since we need to find min(max_left_height, max_right_height), we only need to care about the shorter height,
it doesn't really matter if we find the max(left, right) or not
therefore, we can use two pointer from start and end, and move toward middle, 
while iterating we move the shorter side forward cause we want to find the max height to get the max water

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        max_left = height[0]
        max_right = height[-1]
        left, right = 1, len(height) - 2
        while left <= right:
            if max_left <= max_right:
                ans += max(0, max_left -  height[left])
                max_left = max(height[left], max_left)
                left += 1
            else:
                ans += max(0, max_right - height[right])
                max_right = max(height[right], max_right)
                right -= 1
        return ans