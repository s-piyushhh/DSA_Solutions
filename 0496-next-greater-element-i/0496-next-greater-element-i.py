class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        ans = []
        for num in nums1:
            next = -1
            for i in range(n - 1, -1, -1):
                if nums2[i] > num:
                    next = nums2[i]
                elif nums2[i] == num:
                    break
            ans.append(next)
        return ans