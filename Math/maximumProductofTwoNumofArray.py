'''
Leetcode Problem: 1464. Maximum Product of Two Elements in an Array
Description: Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''


class Solution:
    def maxProduct(self, nums):
        nums.sort(reverse = True)
        return (nums[0]-1) * (nums[1]-1)
    
if __name__ == "__main__":
    nums = [3, 4, 5, 2]
    solution = Solution()
    print(solution.maxProduct(nums))  # Output: 12