"""
Leetcode Problem: 3982
Description:
Given an array of integers nums, return the sum of all elements in nums that have the maximum difference between their maximum and minimum digits. If there are multiple elements with the same maximum difference, return the sum of all such elements.
"""


class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxNum = 0
        ans = 0
        for num in nums:
            maxi = 0
            mini = 100000
            for i in str(num):
                maxi = max(maxi, int(i))
                mini = min(mini, int(i))
            
            digit = maxi- mini

            if digit > maxNum:
                ans = num
                maxNum = digit
            elif digit == maxNum:
                ans += num

        return ans

if __name__ == "__main__":
    # nums = [123, 456, 789, 12, 34]
    nums = [123, 256, 789, 12, 34]
    solution = Solution()
    result = solution.maxDigitRange(nums)
    print(result)