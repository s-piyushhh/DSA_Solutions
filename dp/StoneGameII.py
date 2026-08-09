'''
Leetcode #1140. Stone Game II
Description: Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones. Alice and Bob take turns, with Alice starting first. Initially, M = 1. On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X).    

'''


from functools import cache

class Solution:
    def stoneGameII(self, piles) -> int:
        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]

        @cache
        def dfs(i, M):
            if i + M * 2 >= len(piles):
                return piles[i]

            return piles[i] - min(dfs(i + j, max(M, j)) for j in range(1, M * 2 + 1))

        return dfs(0, 1)


if __name__ == "__main__":
    piles = [2, 7, 9, 4, 4]
    solution = Solution()
    print(solution.stoneGameII(piles))  # Output: 10