"""
My Solution

Use two pointer from start and end, both pointers move toward middle to find iterate the list
compare the height of the pointers and move the shorter one cause we want the most water


Time:
O(N)

Space:
O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > ans:
                ans = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans