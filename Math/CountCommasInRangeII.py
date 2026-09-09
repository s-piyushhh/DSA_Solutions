"""
Leetcode Problem: Count Commas in Range II
Description: Given a number n, return the number of commas that would be used if you wrote out all the numbers from 1 to n in standard decimal notation. For example, if n = 1000, you would write out the numbers 1, 2, 3, ..., 999, 1000. The numbers 1 through 999 do not have any commas, but the number 1000 has one comma. Therefore, the answer would be 1.
"""


class Solution:
    def countCommas(self, n):
        ans = 0
        m = 1
        while n >= (10 ** (3*m)):
            ans += n - (10 ** (3 * m)) + 1
            m += 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countCommas(1000))  # Output: 1
    print(solution.countCommas(2000))  # Output: 1001
    print(solution.countCommas(999))   # Output: 0
    print(solution.countCommas(500))   # Output: 0
    print(solution.countCommas(10000002))  # Output: