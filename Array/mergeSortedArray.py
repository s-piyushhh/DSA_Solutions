"""
Leetcode Problem: 88
Desc: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m-1
        second = n-1
        i = m+n-1
        while first >= 0 and second >= 0:
            if (nums1[first] >= nums2[second]):
                nums1[i] = nums1[first]
                first -= 1
                i -= 1
            else:
                nums1[i] = nums2[second]
                second -= 1
                i -= 1

        while first >= 0:
            nums1[i] = nums1[first]
            first -= 1
            i -= 1

        while second >= 0:
            nums1[i] = nums2[second]
            second -= 1
            i -= 1
        return nums1        
    
    
if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3 
    nums2 = [2, 5, 6] 
    n = 3
    
    # nums1 = [1] 
    # m = 1
    # nums2 = [] 
    # n = 0
    
    # nums1 = [0] 
    # m = 0
    # nums2 = [1]
    # n = 1
    
    ans = obj.merge(nums1, m, nums2, n)
    print(ans)
