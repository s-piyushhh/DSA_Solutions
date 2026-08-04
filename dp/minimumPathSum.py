'''
Leetcode 64. Minimum Path Sum
Description: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        memo = [[-1] * n for _ in range(m)]

        def search(i, j):
            if i == m or j == n:
                return float('inf')

            if i == m-1 and j == n-1:
                return grid[i][j]

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = grid[i][j] + min(search(i+1, j), search(i, j+1))

            return memo[i][j]

        return search(0, 0)

if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    solution = Solution()
    print(solution.minPathSum(grid))  # Output: 7   