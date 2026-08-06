'''
Leetcode Problem: 3345 
Description: Given two positive integers n and t, return the smallest integer greater than or equal to n such that the product of its digits is divisible by t. If there is no such integer, return -1.
'''

class Solution:
    def smallestNumber(self, n, t):
        def isTrue(n):
            prod = 1

            if prod == 0:
                return True

            while n:
                prod *= n % 10
                n = n // 10
            
            return prod % t == 0
        
        while not isTrue(n):
            n += 1

        return n
    
if __name__ == "__main__":
    sol = Solution()
    n = 10
    t = 2
    print(sol.smallestNumber(n, t))  # Output: 10