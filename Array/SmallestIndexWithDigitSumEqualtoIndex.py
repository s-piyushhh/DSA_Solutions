'''
Leetcode 3550. Smallest Index With Digit Sum Equal to Index
Description: Given a 0-indexed integer array nums, return the smallest index i of nums such that the sum of the digits of nums[i] is equal to i. If there is no such index, return -1.
'''

class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            x = nums[i]
            total = 0
            while(x):
                total += x%10
                x = x//10
            
            if(total == i):
                return i
            
        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 10, 11]
    print(solution.smallestIndex(nums))  # Output: 1