class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        m = {}

        for num in nums2:
            while st and num > st[-1]:
                m[st.pop()] = num
            st.append(num)

        while st:
            m[st.pop()] = -1
        
        ans = []
        for i in nums1:
            ans.append(m[i])

        return ans
        