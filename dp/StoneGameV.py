'''
Leetcode 1563. Stone Game V
Description:
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row). Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob will throw away the row which has the maximum value, and Alice's score will be equal to the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. Alice will keep playing until there is only one stone remaining. Return the maximum score that Alice can obtain.
'''


from functools import lru_cache

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefSum = [0] * (n + 1)

        for i in range(n):
            prefSum[i + 1] = prefSum[i] + stoneValue[i]

        @lru_cache(None)
        def Search(l, r):
            if l >= r:
                return 0

            score = 0

            for mid in range(l, r):
                leftSum = prefSum[mid + 1] - prefSum[l]
                rightSum = prefSum[r + 1] - prefSum[mid + 1]

                if leftSum < rightSum:
                    score = max(score, leftSum + Search(l, mid))
                elif leftSum > rightSum:
                    score = max(score, rightSum + Search(mid + 1, r))
                else:
                    score = max(score, leftSum + Search(l, mid),
                                rightSum + Search(mid + 1, r))

            return score

        return Search(0, n - 1)


if  __name__ == "__main__":
    stoneValue = [6, 2, 3, 4, 5, 5]
    print(Solution().stoneGameV(stoneValue))  # Output: 18  