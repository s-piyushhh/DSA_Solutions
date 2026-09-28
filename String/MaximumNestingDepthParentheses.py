'''
Leetcode : 1614. Maximum Nesting Depth of the Parentheses
Description: Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
'''

class Solution:
    def maxDepth(self, s):
        ans = 0
        temp = 0
        for i in s:
            if i == '(':
                temp += 1
            elif i == ')':
                temp -= 1
            ans = max(ans, temp)

        return ans
    
if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"
    solution = Solution()
    result = solution.maxDepth(s)
    print(result)
