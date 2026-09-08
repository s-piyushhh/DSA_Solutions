"""
Leetcode Problem: Count Commas in Range 3870.
"""

class Solution:
    def countCommas(self, n):
        return 0 if n < 999 else n-999
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countCommas(1000))  # Output: 1
    print(solution.countCommas(2000))  # Output: 1001
    print(solution.countCommas(999))   # Output: 0
    print(solution.countCommas(500))   # Output: 0