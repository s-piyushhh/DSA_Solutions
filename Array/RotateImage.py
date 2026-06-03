"""
Leetcode Problem : 48
Desc: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""


class Solution:
    def rotate(self, m):
        n = len(m) - 1
        d = 0

        while d < (n + 1) // 2:
            for i in range(n - 2*d):
                tmp = m[d][d+i]
                m[d][d+i] = m[n-d-i][d]
                m[n-d-i][d] = m[n-d][n-d-i]
                m[n-d][n-d-i] = m[d+i][n-d]
                m[d+i][n-d] = tmp
            d += 1


if __name__ == "__main__":
    obj = Solution()

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    obj.rotate(m)
    print(m)
