"""
leetcode 856: Score of Parentheses
Description: Given a balanced parentheses string s, return the score of the string based on the following rules:
- "()" has score 1.
"""


class Solution:
    def scoreOfParentheses(self, s):
        score_stack = [0]

        for parentheses in s:
            if parentheses == "(":
                score_stack.append(0)
            elif score_stack:
                last_score = score_stack.pop()
                score_stack[-1] += max(1, last_score * 2)

        return score_stack[-1]

if __name__ == "__main__":
    solution = Solution()
    s = "(()(()))"
    result = solution.scoreOfParentheses(s)
    print(f"The score of the balanced parentheses string '{s}' is: {result}")