"""
Leetcode Problem: 115. Distinct Subsequences
Description: Given two strings s and t, return the number of distinct subsequences of s which equals t. 

"""


class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]


if __name__ == "__main__":
    solution = Solution()
    s = "rabbbit"
    t = "rabbit"
    print(solution.numDistinct(s, t))  # Output: 3