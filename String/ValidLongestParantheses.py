'''
Leetcode Problem: 32. Longest Valid Parentheses
Description: Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''


class Solution:
    def longestValidParentheses(self, s):
        res = 0
        st = [-1]
        
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                
                if not st:
                    st.append(i)
                else:
                    res = max(res, i - st[-1])
                    
        return res
    
if __name__ == "__main__":
    s = "(()"
    s1 = ")()())"
    solution = Solution()
    result = solution.longestValidParentheses(s)
    result1 = solution.longestValidParentheses(s1)
    print(result)
    print(result1)