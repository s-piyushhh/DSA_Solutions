"""
Leetcode Problem: 2778 Sum of Squares of Special Elements 
Description: Given a 1-indexed integer array nums, return the sum of squares of special elements in nums. An element nums[i] is called special if i divides n, where n is the length of nums.
"""

class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            if n % (i+1) == 0:
                ans += nums[i]**2

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 2, 3, 4, 5, 6]
    result1 = solution.sumOfSquares(nums1)
    result2 = solution.sumOfSquares(nums2)
    print(result1)  # Output: 21
    print(result2)  # Output: 56