"""
Leetcode Problem: 1
Desc : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in m):
                return [m[target - nums[i]], i]
            m[nums[i]] = i
        # print(m)
        return []

if __name__ == "__main__":
    obj = Solution()

    nums = [2,7,11,15]
    target = 9
    
    # nums = [3,2,4]
    # target = 6
    
    # nums = [3, 3]
    # target = 6
    
    ans = obj.twoSum(nums, target)
    print(ans)
