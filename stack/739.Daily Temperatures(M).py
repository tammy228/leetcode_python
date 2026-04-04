"""
My Solution

use stack to reversed track the temp. and the index,
when finding the warmer temp. we look into stack if st[i] < temp[i] pop it out, till we find the warmer temp.
be careful of while popping out the temp. need to check if the st. is empty or not

Time:
O(N)

Space:
O(N)

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            if i == len(temperatures) - 1:
                st.append((i, temperatures[i]))
                ans.append(0)
            else:
                while st and st[-1][1] <= temperatures[i]:
                    st.pop()
                if not st:
                    ans.append(0)
                else:
                    ans.append(st[-1][0] - i)
                st.append((i, temperatures[i]))
        ans.reverse()
        return ans

"""
Optimize

change from backwards iteration to forward iteration

Time:
O(N)

Space:
O(N)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return ans        