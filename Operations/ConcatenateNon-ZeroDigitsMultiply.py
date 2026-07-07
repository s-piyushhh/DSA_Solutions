'''
Leetcode Problem: 2710. Concatenate Non-Zero Digits in an Integer and Multiply
Description:
Given an integer n, return the result of concatenating the non-zero digits in n and multiplying the result by the sum of the non-zero digits in n.
'''

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        num = ""
        tot = 0
        for i in str(n):
            if i == '0':
                continue
            num += i
            tot += int(i)

        return int(num) * tot

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumAndMultiply(123))