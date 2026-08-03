"""
Leetcode Problem: 63. Unique Paths II
Description: A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). Now consider if some obstacles are added to the grids. How many unique paths would there be?
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        memo = [[-1] * n for _ in range(m)]

        def search(i, j):
            if i == m or j == n:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = search(i+1, j) + search(i, j+1)

            return memo[i][j]

        return search(0, 0)

if __name__ == "__main__":
    solution = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(solution.uniquePathsWithObstacles(obstacleGrid))  # Output: 2