"""
Leetcode Problem: 1979. Find Greatest Common Divisor of Array
Description: Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
"""

class Solution:
    def findGCD(self, nums):
        maxi = max(nums)
        mini = min(nums)

        for i in range(mini, 0, -1):
            if maxi % i == 0 and mini % i == 0:
                return i
        
        return 1
    
if __name__ == "__main__":
    nums = [2, 5, 6, 9, 10]
    solution = Solution()
    result = solution.findGCD(nums)
    print(result)  # Output: 2