"""
Leetcode Problem: 940. Distinct Subsequences II
Description: Given a string s, return the number of distinct non-empty subsequences of s.  
"""


class Solution:
    def distinctSubseqII(self, s):
        mod = 10**9 + 7
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        last = [-1] * 26

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod

            idx = ord(s[i - 1]) - ord('a')

            if last[idx] != -1:
                dp[i] = (dp[i] - dp[last[idx]] + mod) % mod

            last[idx] = i - 1

        return (dp[n] - 1 + mod) % mod

if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    print(solution.distinctSubseqII(s))  # Output: 7