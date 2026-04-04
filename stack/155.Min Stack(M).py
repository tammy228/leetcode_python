"""
My Solution

use two list to keep track of the stack values, and the other the keep track of
the min value of the index

Time:
O(1)

Space:
O(2N)
"""

class MinStack:

    def __init__(self):
        self.st = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_values or self.min_values[-1] >= val:
            self.min_values.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        if val == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
        
"""
Optimize

try to use one list to do both, store as list of list

Time:
O(1)

Space:
O(2N)
"""

class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append([val, val])
        else:
            self.st.append([val, min(val, self.st[-1][1])])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()