'''
Leetcode Problem 1480: Running Sum of 1d Array
Description:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
'''


class Solution:
    def runningSum(self, nums):
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i-1] + nums[i])

        return ans

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.runningSum(nums))  # Output: [1, 3, 6, 10]