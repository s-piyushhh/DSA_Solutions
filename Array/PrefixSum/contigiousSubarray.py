"""
Leetcode Problem 525: Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
Example 1:
Input: nums = [0,1]
"""

class Solution:
    def findMaxLength(self, nums):
        m = {0 : -1}
        zeros = 0
        ones = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 0: zeros += 1
            else: ones += 1

            if (zeros - ones) in m:
                ans = max(ans, i - m[zeros - ones])
            else:
                m[zeros - ones] = i

        return ans
    
    
if __name__ == "__main__":
    nums = [0, 1]
    solution = Solution()
    print(solution.findMaxLength(nums))  # Output: 2