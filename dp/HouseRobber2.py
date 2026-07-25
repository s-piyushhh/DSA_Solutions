"""
Leetcode Problem: 213. House Robber II
Description: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
"""


class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        def robLine(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                curr = max(prev1, num + prev2)

                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            robLine(nums[:-1]),  # exclude last
            robLine(nums[1:])    # exclude first
        )

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([2, 3, 2]))  # Output: 3
    print(solution.rob([1, 2, 3, 1]))  # Output: 4
    print(solution.rob([0]))  # Output: 0