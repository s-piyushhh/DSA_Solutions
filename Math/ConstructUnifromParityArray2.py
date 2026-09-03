"""
Leetcode Problem: 3876. Construct Uniform Parity Array II
Description: You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]​​​​​​​
nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
Return true if it is possible to construct such an array, otherwise return false.
"""


class Solution:
    def uniformArray(self, nums1):
        odds = 0
        evens = 0
        for i in nums1:
            if i % 2 == 0:
                evens += 1
            else:
                odds += 1
        
        if odds == 0 or evens == 0:
            return True
        
        if min(nums1) % 2 == 1:
            return True
        
        return False
    

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    print(solution.uniformArray(nums1))  # Output: True