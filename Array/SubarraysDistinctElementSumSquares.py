"""
Leetcode Problem: 2931 Subarrays Distinct Element Sum of Squares I
Description: Given an integer array nums, return the sum of the squares of the number of distinct elements in all non-empty subarrays of nums.
"""

class Solution:
    def sumCounts(self, nums):
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                ans.append(len(set(nums[i:j]))**2)
        return sum(ans)
    
if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.sumCounts(nums)
    print(result)  # Output: 14