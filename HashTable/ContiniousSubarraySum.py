"""Leetcode 523. Continuous Subarray Sum
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] is a continuous subarray of size 2 whose elements sum up to 6.
"""

class Solution:
    def checkSubarraySum(self, nums, k):
        m = {0 : -1}
        tot = 0
        if len(nums) < 2:
            return False
        for i, num in enumerate(nums):
            tot += num
            if (tot % k) in m:
                if i - m[tot % k] > 1:
                    return True
            else:
                m[tot % k] = i

        return False

if __name__ == "__main__":
    nums = [23, 2, 4, 6, 7]
    k = 6
    solution = Solution()
    result = solution.checkSubarraySum(nums, k)
    print(result)  # Output: True   