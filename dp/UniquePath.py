'''
Leetcode Problem: 62
Desc: There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''


from functools import cache
class Solution:
    def uniquePaths(self, m, n, i = 0, j = 0) -> int:
        @cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0,0)
    

if __name__ == "__main__":
    obj = Solution()
    m, n = 3, 7
    # m,n = 3, 2
    
    ans = obj.uniquePaths(m, n)
    print(ans)
