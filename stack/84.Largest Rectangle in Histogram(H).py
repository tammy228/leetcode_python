"""
Optimize

In order to find to largest rectangle, we need height to be increasing order
Therefore, we can use monotonic stack to do the logic, 
if we met height[i] < height[i-1], we need to pop the height and caculate the area till height[i] >= stack.top()
after iterating all heights, we need to caculate the rest heights in the stack

Time:
O(2N) = O(N)

Space:
O(N)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] #[idx, height]
        max_area = 0
        for idx, height in enumerate(heights):
            last_idx = idx
            while st and st[-1][1] > height:
                max_area = max(max_area, (idx - st[-1][0]) * st[-1][1])
                last_idx = st[-1][0]
                st.pop()
            st.append((last_idx, height))
        
        for idx, height in st:
            max_area = max(max_area, (len(heights) - idx) * height)
        return max_area

"""
Optimize 2

Add a "Sentinel Value" to the height to prevent from writing second for loop
It is only for clean code

Time:
O(2N) = O(N)

Space:
O(N)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] #[idx, height] 
        heights.append(0)
        max_area = 0
        for idx, height in enumerate(heights):
            last_idx = idx
            while st and st[-1][1] > height:
                max_area = max(max_area, (idx - st[-1][0]) * st[-1][1])
                last_idx = st[-1][0]
                st.pop()
            st.append((last_idx, height))
        
        return max_area