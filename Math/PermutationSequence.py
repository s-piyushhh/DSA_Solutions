'''
Leetcode Problem: 60. Permutation Sequence
Description: The set [1, 2, 3, ..., n] contains a total of n! unique permutations. By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
'''

from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        ans = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            x = k // fact
            ans.append(nums.pop(x))
            k %= fact

        return "".join(ans)

if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 3
    print(sol.getPermutation(n, k))  # Output: "213"