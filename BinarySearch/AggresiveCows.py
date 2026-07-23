"""
GFG PRoblem: Aggressive Cows
Description: Given an array of integers representing the positions of stalls and an integer k representing the number of cows, the task is to place the cows in the stalls such that the minimum distance between any two cows is maximized. The function aggressiveCows takes in the list of stall positions and the number of cows, and returns the maximum minimum distance possible between any two cows.
Example:
Input: stalls = [1, 2, 4, 8, 9], k = 3
"""


class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)

        def helper(mid):
            cowsPlaced = 1
            last = stalls[0]
            for i in range(n):
                if stalls[i] - last >= mid:
                    cowsPlaced += 1
                    last = stalls[i]
            if cowsPlaced >= k:
                return True
            return False

        l = 1
        r = stalls[-1] - stalls[0]

        ans = 0
        while l <= r:
            mid = (l + r) >> 1

            if helper(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        return ans

if __name__ == "__main__":
    stalls = [1, 2, 4, 8, 9]
    k = 3
    solution = Solution()
    print(solution.aggressiveCows(stalls, k))  # Output: 3