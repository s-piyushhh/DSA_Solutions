"""
Leetcode Problem: 3524 
Description: You are given an array of positive integers nums, and a positive integer k.
You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.
You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.
Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.
"""

class Solution:
    def resultArray(self, nums, k):
        n = len(nums)
        result = [0] * k
        # Initial state: no elements have been processed, so no non-empty subarray exists.
        dp = [0] * k

        for i in range(n):
            ndp = [0] * k  # Current state (rolling array).

            ndp[nums[i] % k] += 1

            for r in range(k):
                ndp[(r * nums[i]) % k] += dp[r]

            dp = ndp  # Update the state.

            # Accumulate the answer.
            for r in range(k):
                result[r] += dp[r]
        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(solution.resultArray(nums, k))  # Example usage