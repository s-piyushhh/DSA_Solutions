"""
Leetcode Problem: 2581. Count the Number of Beautiful Subarrays
Description: You are given two integers n and k. You have n points on a 1-D plane labeled from 0 to n-1. You are asked to draw k non-overlapping line segments such that each segment covers two points. A line segment is represented by a pair of points (i, j) where 0 <= i < j < n.
"""

from functools import lru_cache
class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        @lru_cache(None)
        def dp(i, k, isStart):
            if k == 0: return 1 # Found a way to draw k valid segments
            if i == n: return 0 # Reach end of points
            ans = dp(i+1, k, isStart) # Skip ith point
            if isStart:
                ans += dp(i+1, k, False) # Take ith point as start
            else:
                ans += dp(i, k-1, True) # Take ith point as end
            return ans % MOD
        return dp(0, k, True)
    
if __name__ == "__main__":
    solution = Solution()
    n = 5
    k = 2
    print(solution.numberOfSets(n, k))