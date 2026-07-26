'''
Leetcode Problem: 4000
Description: Given two integers n and s, find the largest integer of length n such that the sum of its digits is equal to s. If no such integer exists, return -1.
'''


class Solution:
    def largestInteger(self, n, s):
        if s / n > 9:
            return -1

        ans = 0

        for i in range(n):
            temp = min(9, s)
            ans = ans*10 + temp
            s -= temp

        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestInteger(3, 20))  # Output: 992
    print(solution.largestInteger(2, 10))  # Output: 91
    print(solution.largestInteger(2, 19))  # Output: -1