"""
LeetCode Problem : 15
Desc: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1
        return ans

if __name__ == "__main__":
    
    obj = Solution()
    
    nums = [-1, 0,1,2,-1,-4]
    # nums = [0, 0,0]
    
    ans = obj.threeSum(nums)
    
    print(ans)