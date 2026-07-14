"""
Leetcode Problem: 560. Subarray Sum Equals K
Description: Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

"""

class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        sum = 0
        m = {}

        for i, num in enumerate(nums):
            sum += num
            if sum == k:
                ans = max(ans, i+1)

            if sum-k in m:
                ans = max(ans, i - m[sum-k])
            else:
                m[sum] = i

        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))  # Output: 2
    print(solution.subarraySum([1, 2, 3], 3))  # Output: 2
    print(solution.subarraySum([1, -1, 0], 0)) # Output: 3