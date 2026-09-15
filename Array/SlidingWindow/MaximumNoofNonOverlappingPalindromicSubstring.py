"""
Leetcode Problem: 2472. Maximum Number of Non-overlapping Palindrome Substrings
Description: Given a string s and an integer k, return the maximum number of non-empty palindromic substrings of length at least k that can be found in s. The substrings must be non-overlapping.
"""

class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        if k == 1:
            return n

        res = i = 0

        while i <= n - k:
            for d in (k, k + 1):
                if i + d <= n and s[i: i + d] == s[i: i + d][::-1]:
                    res += 1
                    i += d
                    break
            else:
                i += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    s = "ababa"
    k = 3
    print(solution.maxPalindromes(s, k))  # Output: 1