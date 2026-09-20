"""
Leetcode Problem: Reverse Degree of String 3498
Description: Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:

For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
Sum these products for all characters in the string.
Return the reverse degree of s.
"""


class Solution:
    def reverseDegree(self, s):
        ans = 0
        for i, c in enumerate(s):
            # temp = ord('z') - ord(c) + 1
            ans += (ord('z') - ord(c) + 1) * (i + 1)

        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    print(solution.reverseDegree(s))  # Output: 148