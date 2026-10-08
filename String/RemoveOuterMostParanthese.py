'''
Leetcode Problem: 1021. Remove Outermost Parentheses
Description: A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation. For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
'''

class Solution:
    def removeOuterParentheses(self, s):
        res, lvl = [], 0

        for c in s:
            if c == ")":
                lvl -= 1
            if lvl > 0:
                res.append(c)
            if c == "(":
                lvl += 1

        return "".join(res)

if __name__ == "__main__":
    s = "(()())(())"
    solution = Solution()
    result = solution.removeOuterParentheses(s)
    print(result)  # Output: "()()()"