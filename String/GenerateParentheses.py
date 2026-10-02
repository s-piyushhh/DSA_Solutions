"""
Leetcode Problem: 22. Generate Parentheses
Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]

        n -= 1
        res = []

        def dfs(O, C, s):
            if not O and not C:
                res.append(s + ")")
                return

            if O > 0:
                dfs(O - 1, C, s + "(")

            if C >= O:
                dfs(O, C - 1, s + ")")

        dfs(n, n, "(")

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))