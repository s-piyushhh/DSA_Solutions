'''
Leetcode 1872. Stone Game VIII
Description: Alice and Bob take turns playing a game with a row of stones. There are n stones arranged in a row, and each stone has an associated value given in the integer array stones.
On each player's turn, that player can remove the leftmost stone from the row and receive points equal to the sum of the values of all remaining stones in the row. The game continues until there is only one stone left in the row, at which point the player with the most points wins.
'''

from itertools import accumulate
class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        pre = list(accumulate(stones))
        f = [0] * n
        f[n - 1] = pre[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], pre[i] - f[i + 1])
        return f[1]


if __name__ == "__main__":
    stones = [7, -6, 5, 10, 5, -2, -6]
    solution = Solution()
    result = solution.stoneGameVIII(stones)
    print(result)  # Output: 13