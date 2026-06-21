"""
LC Problem: 4
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1)
        if n % 2 == 1:
            return float(nums1[n // 2])
        else:
            x = nums1[n // 2 - 1]
            y = nums1[n // 2]
            return (float(x) + float(y)) / 2.0


if __name__ == "__main__":
    obj = Solution1()

    # nums1 = [1, 3]
    # nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]

    ans = obj.findMedianSortedArrays(nums1, nums2)

    print(ans)
