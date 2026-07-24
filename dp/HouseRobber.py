"""
Leetcode Problem: 198. House Robber
Description: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example: 
Input: nums = [1,2,3,1]
Output: 4   
"""



class Solution:
    def rob(self, nums):
        m = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in m:
                return m[i]

            m[i] = nums[i] + max(dfs(i+2), dfs(i+3))

            return m[i]

        return max(dfs(0), dfs(1))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    solution = Solution()
    print(solution.rob(nums))  # Output: 4