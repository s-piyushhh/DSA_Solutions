"""
Leetcode Problem: 4006
Description: You are given a binary string s.
A prefix of s is considered valid if its characters can be rearranged to form an alternating string.
Return the number of valid prefixes of s.
A binary string is a string consisting only of '0' and '1'.
A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.
A substring is a contiguous non-empty sequence of characters within a string.
A string is considered alternating if no two adjacent characters are equal.
"""

class Solution:
    def countValidPrefixes(self, s):
        zeros = 0
        ones = 0
        ans = 0
        for i in s:
            if i == '0':
                zeros += 1
            else:
                ones += 1

            if abs(zeros - ones) <= 1:
                ans += 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "1101001"
    result = solution.countValidPrefixes(s)
    print(f"The number of valid prefixes in the binary string '{s}' is: {result}")