'''
Leetcode problem: 3857
Description: Given an integer n, return the minimum cost to split it into ones. The cost of splitting an integer x into two integers a and b is defined as a * b. You can split the integer multiple times until you have only ones.

'''

class Solution:
    def minCost(self, n: int) -> int:
        ans = 0
        for i in range(n):
            ans += i
        return ans

if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(solution.minCost(n))  # Output: 10
    