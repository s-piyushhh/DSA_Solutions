"""
Leetcode Problem: 1190. Reverse Substrings Between Each Pair of Parentheses
Description: You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
"""

class Solution:
    def reverseParentheses(self, s):
        n = len(s)
        link = [0] * n
        stk = res = []

        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                j = stk.pop()
                link[i] = j
                link[j] = i

        dr, i = 1, 0
        while i < n:
            if s[i] >= 'a':
                res.append(s[i])
            else:
                i = link[i]
                dr = -dr

            i += dr

        return ''.join(res)
    
if __name__ == "__main__":
    solution = Solution()
    s1 = "(abcd)"
    s2 = "(ed(et(oc))el)"
    result1 = solution.reverseParentheses(s1)
    result2 = solution.reverseParentheses(s2)
    print(result1)
    print(result2)