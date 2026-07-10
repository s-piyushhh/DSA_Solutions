"""
Leetcode Problem: 121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

"""

class Solution:
    def maxProfit(self, prices):
        ans = 0
        currMin = prices[0]

        for i in prices:
            if i >= currMin:
                ans = max(ans, i - currMin)
            else:
                currMin = i
        return ans

if __name__ == "__main__":
    obj = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7,6,4,3,1]

    ans = obj.maxProfit(prices)

    print(ans)
