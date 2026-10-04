'''
Leetcode Problem: 678. Valid Parenthesis String
Description: Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
'''


class Solution:
    def checkValidString(self, s):
        l = h = 0

        for c in s:
            l += ((c == '(') << 1) - 1
            h += ((c != ')') << 1) - 1

            if h < 0:
                return False

            l = max(l, 0)

        return l == 0

if __name__ == "__main__":
    s = "(*))"
    solution = Solution()
    print(solution.checkValidString(s))  # Output: True