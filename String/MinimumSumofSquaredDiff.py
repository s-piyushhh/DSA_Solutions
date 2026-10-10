"""
Leetcode Problem: 2333. Minimum Sum of Squared Difference
Description: You are given two positive integer arrays nums1 and nums2, both of length n, and two positive integers k1 and k2. You can perform the following operation on nums1 or nums2 exactly k1 times on nums1 and exactly k2 times on nums2:
Choose an index i (0 <= i < n) and replace nums1[i] with nums1[i] + 1 or nums1[i] - 1.
Choose an index i (0 <= i < n) and replace nums2[i] with nums   2[i] + 1 or nums2[i] - 1.
The squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])^2 for each 0 <= i < n. Return the minimum squared difference after performing the operations.   
"""


class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        d = [0] * 100001
        k = k1 + k2
        total = 0
        mx = 0

        # Step 1: count the differences
        for a, b in zip(nums1, nums2):
            x = abs(a - b)
            d[x] += 1
            total += x
            mx = max(mx, x)

        # Enough budget -> every difference becomes 0
        if total <= k:
            return 0

        # Step 2: shave the biggest differences, level by level
        for i in range(mx, 0, -1):
            if k <= 0:
                break
            move = min(k, d[i])
            d[i] -= move
            d[i - 1] += move
            k -= move

        # Step 3: add up the squares
        ans = 0
        for i in range(mx + 1):
            ans += i * i * d[i]

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k1 = 3
    k2 = 3
    result = solution.minSumSquareDiff(nums1, nums2, k1, k2)
    print(result)  # Output: 0