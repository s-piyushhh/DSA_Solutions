"""
leetcode 238. Product of Array Except Self
Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

"""


class Solution:
    def productExceptSelf(self, nums):
        left = 1
        temp = 1
        right = []
        ans = []

        for i in range(len(nums)-1, 0, -1):
            temp = temp * nums[i]
            right.append(temp)
        right = right[::-1]

        for i in range(len(nums)-1):
            ans.append(left * right[i])
            left *= nums[i]

        ans.append(left)
        return ans
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]