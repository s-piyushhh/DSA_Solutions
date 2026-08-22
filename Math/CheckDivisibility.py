'''
Leetcode Problem: 3622 Check Divisibility by Digit Sum and Product
Description: Given a positive integer n, check whether it is divisible by the sum of its digits plus the product of its digits. Return true if it is divisible, otherwise return false.
'''

class Solution:
    def checkDivisibility(self, n):
        sum = 0
        prod = 1
        x = n
        while (x):
            sum += x % 10
            prod *= x % 10
            x = x//10

        return n % (sum + prod) == 0

if __name__ == "__main__":
    solution = Solution()
    n = 12
    result = solution.checkDivisibility(n)
    print(result)  # Output: True