'''
Leetcode Problem: 73
Desc: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
'''


class Solution:
    def setZeroes(self, matrix):
        row = set()
        col = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0


if __name__ == "__main__":
    obj = Solution()

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    obj.setZeroes(matrix)
    print(matrix)
