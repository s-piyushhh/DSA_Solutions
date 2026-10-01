'''
Leetcode Problem: 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
Description: Given a valid parentheses string, split it into two valid parentheses strings such that the maximum nesting depth of the two strings is minimized.
'''

class Solution:
    def maxDepthAfterSplit(self, seq):
        d = 0
        ans = []
        for i in seq:
            if i == '(':
                d += 1
                ans.append(d % 2)
            else:
                ans.append(d % 2)
                d -= 1

        return ans


if __name__ == "__main__":
    seq = "(()())"
    solution = Solution()
    print(solution.maxDepthAfterSplit(seq))  # Output: [0, 1, 1, 1, 1, 0]