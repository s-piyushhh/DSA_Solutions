'''
Leetcode Problem: 3857. Minimum Cost to Split an Array
'''

class Solution:
    def minCost(self, n):
        return n * (n - 1) // 2
    
if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(solution.minCost(n))  # Output: 10