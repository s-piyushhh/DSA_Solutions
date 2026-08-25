'''
Leetcode Problem: Smallest Missing Multiple of K
Given an integer array nums and an integer k, return the smallest positive integer that is a multiple of k and does not appear in nums.
Example 1:
Input: nums = [2,3,4], k = 2
Output: 6
Explanation: The smallest multiple of 2 that does not appear in nums is 6.
'''

class Solution:
    def missingMultiple(self, nums, k):
        nums = set(nums)
        rnge = (100//k)
        for i in range(1, rnge+1):
            if k*i not in nums:
                return k*i
        return k * (rnge+1)
    

if __name__ == "__main__":
    nums = [2, 3, 4]
    k = 2
    solution = Solution()
    result = solution.missingMultiple(nums, k)
    print(result)  # Output: 6