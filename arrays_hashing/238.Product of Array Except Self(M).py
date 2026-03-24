
"""
My Solution

first decompose each element and find pattern, we can shift 1 to continue product from left to right then 
after right to left to get the final result
Ex:
[1,2,3,4]
decompose: [2*3*4, 1*3*4, 1*2*4, 1*2*3]
left -> right: [1, 1, 2, 6]
right -> left: [24,12,4,1]

Time:
O(N)

Space:
O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]* len(nums)
        num = 1
        for i in range(len(nums)):
            ans[i] = num
            num *= nums[i]
            
        num = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= num
            num *= nums[i]
            
        return ans