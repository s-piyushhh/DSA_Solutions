'''
Leetcode Problem: 1658. Minimum Operations to Reduce X to Zero  
Description: You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations. Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''

class Solution:
    def minOperations(self, nums, x):
        def search(i, j, x, m):
            if x == 0:
                return 0

            if i > j or x < 0:
                return float("inf")

            if (i, j) in m:
                return m[(i, j)]

            takeLeft = 1 + search(i+1, j, x - nums[i], m)
            takeright = 1 + search(i, j-1, x - nums[j], m)

            m[(i, j)] = min(takeLeft, takeright)
            return m[(i, j)]

        m = {}
        ans = search(0, len(nums)-1, x, m)

        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    nums = [1, 1, 4, 2, 3]
    x = 5
    solution = Solution()
    print(solution.minOperations(nums, x))  # Output: 2