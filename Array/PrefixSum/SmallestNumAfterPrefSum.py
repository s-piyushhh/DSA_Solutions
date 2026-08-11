'''
Leetcode Problem: 2996 
Description: Given an array of integers nums, return the smallest positive integer that is missing from the prefix sum of the array. The prefix sum of an array is defined as the sum of its elements up to a certain index.
'''


class Solution:
    def missingInteger(self, nums):
        prefSum = nums[0]
        i = 1
        while i < len(nums) and nums[i] - nums[i-1] == 1:
            prefSum += nums[i]
            i += 1

        nums = set(nums)

        while True:
            if prefSum not in nums:
                return prefSum
            prefSum += 1

        return 0

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    print(sol.missingInteger(nums))  # Output: 6

    nums = [1, 2, 3, 5]
    print(sol.missingInteger(nums))  # Output: 4

    nums = [1, 2, 3, 4, 6]
    print(sol.missingInteger(nums))  # Output: 5

    nums = [1, 2, 3, 4, 5, 7]
    print(sol.missingInteger(nums))  # Output: 6