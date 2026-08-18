'''
Leetcode Problem: 3471 ]
Description:You are given an integer array nums and an integer k.
An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
Return the largest almost missing integer from nums. If no such integer exists, return -1.
A subarray is a contiguous sequence of elements within an array.
'''

class Solution:
    def largestInteger(self, nums, k):
        m = {}
        n = len(nums)
        for i in nums:
            m[i] = m.get(i, 0) + 1

        left = nums[0]
        right = nums[-1]

        if n == k:
            return max(nums)

        if k == 1:
            maxi = -1
            for i in nums:
                if m[i] == 1:
                    maxi = max(maxi, i)
            if maxi > -1:
                return maxi

        if m[left] > 1 and m[right] > 1:
            return -1
        elif m[left] > 1:
            return right
        elif m[right] > 1:
            return left

        return max(left, right)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(Solution().largestInteger(nums1, k1))
    nums2 = [3,9,2,1,7]
    k2= 3
    print(Solution().largestInteger(nums2, k2))
    
      # Output: 5