'''
Leetcode Problem: 540
Desc: You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
'''


class Solution:
    def singleNonDuplicate(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid

        return nums[l]


if __name__ == "__main__":
    obj = Solution()

    # nums = [1,1,2,3,3,4,4,8,8]
    nums = [3, 3, 7, 7, 10, 11, 11]

    ans = obj.singleNonDuplicate(nums)

    print(ans)
