"""
Desc:Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
Return the maximum value as a double, rounded to 6 decimal places.
"""

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        # code here
        factor = []
        for i in range(len(val)):
            factor.append(val[i] / wt[i])

        x = list(zip(val, wt, factor))

        ans = 0

        x.sort(key=lambda n: n[2], reverse=True)

        for i, j, k in x:
            if j <= capacity:
                ans += i
                capacity -= j
            elif j > capacity:
                # ans += i * capacity / j
                ans += k * capacity
                break
            # print(ans)

        return round(ans, 6)


if __name__ == "__main__":

    obj = Solution()

    val = [60, 100, 120]
    wt = [10, 20, 30]
    capacity = 50
    
    # val = [500]
    # wt = [30]
    # capacity = 10
    
    ans = obj.fractionalKnapsack(val, wt, capacity)

    print(ans)
