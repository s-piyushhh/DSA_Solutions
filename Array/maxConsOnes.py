"""
Leetcode Problem: 485
Desc: Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0

        return ans


if __name__ == "__main__":

    obj = Solution()

    nums = [1, 1, 0, 1, 1, 1]
    # nums = [1, 0, 1, 1, 0, 1]
    ans = obj.findMaxConsecutiveOnes(nums)

    print(ans)
