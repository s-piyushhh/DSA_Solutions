"""
Leetcode Problem: 242. Valid Anagram
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

"""


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        m = {}
        for i in s:
            m[i] = m.get(i, 0) + 1

        for i in t:
            if i in m:
                m[i] -= 1
            else:
                return False

            if m[i] < 0:
                return False

        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))  # Output: True

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))  # Output: False