"""
Leetcode Problem: 1541. Minimum Insertions to Balance a Parentheses String
Description: Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
"""


class Solution:
    def minInsertions(self, s):
        open = ans = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
            else:
                # Step 1: make a "))"
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                # Step 2: find its '('
                if open > 0:
                    open -= 1
                else:
                    ans += 1
            i += 1

        return ans + open * 2
    
if __name__ == "__main__":
    solution = Solution()
    s = "(()))"
    print(solution.minInsertions(s))  # Output: 1