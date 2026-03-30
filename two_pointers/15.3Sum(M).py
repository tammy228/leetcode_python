"""
My Solution

Use two sum sorted method and extend to three sum
1. sort the array
2. for each number use two pointer to find the combinations

Time:
O(Nlogn + N^2)

Space:
O(1), but python sort() (timsort) O(N), C++ std::sort()(Introsort, based on quick sort) O(logN)

"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            two_sum = 0 - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                lr_sum = nums[left] + nums[right]
                if lr_sum == two_sum:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
                elif lr_sum < two_sum:
                    left += 1
                else:
                    right -= 1
        return ans

"""
Optimize

Add nums[i] > 0 for early stoping, due to the array is sorted if nums[i] > 0 there is no combinations for solution
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            if (i > 0 and num == nums[i-1]) or num > 0:
                continue
            two_sum = 0 - num
            left, right = i + 1, len(nums) - 1
            while left < right:
                lr_sum = nums[left] + nums[right]
                if lr_sum == two_sum:
                    ans.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
                elif lr_sum < two_sum:
                    left += 1
                else:
                    right -= 1
                
        return ans