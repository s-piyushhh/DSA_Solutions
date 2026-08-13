'''
Leetcode 1690. Stone Game VII
Description: 
'''



from functools import lru_cache
class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]

        def getSum(left, right):
            return preSum[right + 1] - preSum[left]

        @lru_cache(2000)
        def dp(left, right, isAlice):
            if left == right:
                return 0  # only 1 store, score = 0

            if isAlice:
                a = dp(left + 1, right, not isAlice) + \
                    getSum(left + 1, right)  # Take leftmost
                b = dp(left, right - 1, not isAlice) + \
                    getSum(left, right - 1)  # Take rightmost
                return max(a, b)
            else:
                a = dp(left + 1, right, not isAlice) - \
                    getSum(left + 1, right)  # Take leftmost
                b = dp(left, right - 1, not isAlice) - \
                    getSum(left, right - 1)  # Take rightmost
                return min(a, b)

        return dp(0, n - 1, True)


if __name__ == "__main__":
    stones = [5, 3, 1, 4, 2]
    solution = Solution()
    result = solution.stoneGameVII(stones)
    print(result)  # Output: 6