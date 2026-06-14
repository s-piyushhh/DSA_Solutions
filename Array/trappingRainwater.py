"""
Leetcode Problem : 42
Desc: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height):
        n = len(height)
        l = 0
        r = n - 1
        lmax = height[l]
        rmax = height[r]
        ans = 0
        while l <= r:
            if lmax < rmax:
                ans += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                ans += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])

        return ans


if __name__ == "__main__":

    obj = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 0, 3, 2, 5]
    
    ans = obj.trap(height)

    print(ans)
