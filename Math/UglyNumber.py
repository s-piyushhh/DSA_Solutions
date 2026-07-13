'''
Leetcode Problem: 263. Ugly Number
Description: An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''


class Solution:
    def isUgly(self, n):
        if n == 0:
            return False
        
        while n % 2 == 0:
            n = n / 2 
        while n % 3 == 0:
            n = n / 3 
        while n % 5 == 0:
            n = n / 5 

        if n == 1:
            return True
        
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isUgly(6))  # Output: True
    print(solution.isUgly(8))  # Output: True
    print(solution.isUgly(14)) # Output: False