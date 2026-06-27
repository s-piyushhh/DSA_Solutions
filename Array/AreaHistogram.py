'''
Leetcode Problem: 84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''

class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        nextSmaller = [n] * n
        st = []

        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                nextSmaller[i] = st[-1]

            st.append(i)

        lastSmaller = [-1] * n
        st = []

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                lastSmaller[i] = st[-1]

            st.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (nextSmaller[i] - lastSmaller[i] - 1))

        return ans


if __name__ == "__main__":
    obj = Solution()

    heights = [2, 1, 5, 6, 2, 3]
    # heights = [2,4]
    # heights = [2,1,2]

    ans = obj.largestRectangleArea(heights)

    print(ans)