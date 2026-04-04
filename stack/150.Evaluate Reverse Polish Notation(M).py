"""
My Solution

Use stack to do the logic
if met number push to stack, else pop the number and do the logic

Time: 
O(N)

Space:
O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in["*", "/", "+", "-"]:
                st.append(int(token))
            else:
                second_num = st.pop()
                first_num = st.pop()
                if token == "+":
                    val = first_num + second_num
                elif token == "-":
                    val = first_num - second_num
                elif token == "*":
                    val = first_num * second_num
                else:
                    val = int(first_num / second_num)
                st.append(val)
        return st[-1]