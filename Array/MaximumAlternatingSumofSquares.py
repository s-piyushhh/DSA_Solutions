"""
Leetcode Problem: 3727 Maximum Alternating Sum of Squares
Description :You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

"""


class Solution:
    def maxAlternatingSum(self, nums):
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        nums.sort()

        n = len(nums)
        print(nums)

        ans = 0
        if n % 2 != 0:
            ans = nums[n//2]*nums[n//2]

        for i in range(n//2):
            ans += nums[n-1-i]**2 - nums[i]**2
        

        return ans        
    
if __name__ == "__main__":
    nums = [4, 2, 5, 3]
    solution = Solution()
    result = solution.maxAlternatingSum(nums)
    print(result)  # Output: 34