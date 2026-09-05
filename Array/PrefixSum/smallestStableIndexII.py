"""
Leetcode Problem: 3903 Smallest Stable index II
Description: Given an integer array nums and an integer k, return the smallest index i such that the difference between the maximum value in nums[0..i] and the minimum value in nums[i..n-1] is less than or equal to k. If no such index exists, return -1.
"""

class Solution:
    def firstStableIndex(self, nums, k):
        suf = [0] * len(nums)
        mini = 10 ** 9
        for i in range(len(nums)-1, -1, -1):
            mini = min(mini, nums[i])
            suf[i] = mini

        maxi = 0
        for i in range(len(nums)):
            maxi = max(maxi, nums[i])
            if maxi - suf[i] <= k:
                return i
            # print(maxi, suf[i])
        return -1

if __name__ == "__main__":
    nums = [5, 0, 1, 4]
    k = 3
    solution = Solution()
    result = solution.firstStableIndex(nums, k)
    print(result)  # Output: 3