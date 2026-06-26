'''
You are given an integer array arr[ ]. For every element in the array, your task is to determine its Next Smaller Element (NSE).


The Next Smaller Element (NSE) of an element x is the first element that appears to the right of x in the array and is strictly smaller than x.

If no such element exists, assign -1 as the NSE for that position.
Examples:

Input: arr[] = [4, 8, 5, 2, 25]
Output: [2, 5, 2, -1, -1]
'''



class Solution:
    def nextSmallerEle(self, arr):
        st = []
        n = len(arr)
        ans = [-1] * n

        for i in range(n - 1, -1, -1):
            while st and arr[i] <= st[-1]:
                st.pop()

            if st:
                ans[i] = st[-1]
            else:
                ans[i] = -1

            st.append(arr[i])

        return ans


if __name__ == "__main__":
    obj = Solution()

    st = [4, 8, 5, 2, 25]

    ans = obj.nextSmallerEle(st)
    print(ans)
