"""
Leetcode Problem: 58. Length of Last Word
Description: Given a string s consisting of words and spaces, return the length of the last word in the string. A word is defined as a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                continue
            else:
                return len(s) - i - 1

        return len(s)

if __name__ == "__main__":
    obj = Solution()
    s = "Hello World"
    print(obj.lengthOfLastWord(s))  # Output: 5