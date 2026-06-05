"""
Leetcode Problem: 50
Desc: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


class Solution:
    def pow(self, x, n):
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            ans = helper(x, n//2)
            ans = ans * ans
            if n % 2:
                return x * ans
            return ans

        ans = helper(x, abs(n))
        if n < 0:
            return 1/ans
        return ans
    
    
if __name__ == "__main__":
    obj = Solution()
    x = 2
    n = 10
    
    # x = 2.1
    # n = 3
    
    # x = 2
    # n = -2
    
    ans = obj.pow(x, n)
    print(ans)