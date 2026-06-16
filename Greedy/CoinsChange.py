"""
Leetcode Problem: 322
Desc: You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""
from math import inf


class Solution:
    def coinChange(self, coins, amount):

        def helper(i, amount):
            if amount == 0:
                return 0

            if i < 0:
                return inf

            if coins[i] > amount:
                return helper(i-1, amount)

            take = 1 + helper(i, amount - coins[i])
            skip = helper(i - 1, amount)

            return min(take, skip)

        ans = helper(len(coins)-1, amount)

        return ans if ans != inf else -1




if __name__ == "__main__":

    obj = Solution()

    coins = [1, 2, 5]
    amount = 11
    # coins = [2]
    # amount = 3

    ans = obj.coinChange(coins, amount)

    print(ans)
