'''
Leetcode Problem: 921. Minimum Add to Make Parentheses Valid
Description: Given a string s of '(' and ')', return the minimum number of parentheses we must add to make the resulting string valid.
'''

class Solution:
    def minAddToMakeValid(self, s):
        brackets = 0
        ans = 0
        for i in s:
            if i == '(':
                brackets += 1
            else:
                if brackets == 0:
                    ans += 1
                else:
                    brackets -= 1

        ans += brackets
        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "())"
    result = solution.minAddToMakeValid(s)
    print(f"The minimum number of parentheses to add to make the string '{s}' valid is: {result}")