'''
Leetcode Problem: 740. Delete and Earn
Description: Given an array nums of integers, you can perform operations on the array. In each operation, you pick any nums[i] and delete it to earn nums[i] points. Afterward, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
'''
class Solution:
    def deleteAndEarn(self, nums):
        maxiNum = max(nums)
        x = [0] * (maxiNum + 1)

        for i in nums:
            x[i] += i

        m = {}

        def search(i):
            if i >= len(x):
                return 0

            if i in m:
                return m[i]

            take = x[i] + search(i+2)
            skip = search(i+1)

            m[i] = max(take, skip)

            return m[i]

        return search(0)

if __name__ == "__main__":
    nums = [3, 4, 2]
    solution = Solution()
    result = solution.deleteAndEarn(nums)
    print(result)  # Output: 6