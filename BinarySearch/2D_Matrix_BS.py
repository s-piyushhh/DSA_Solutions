"""
Leetcode Problem: 74
Desc : You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        h = m * n - 1

        while l <= h:
            mid = l + (h - l)//2
            r = mid // n
            c = mid % n

            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                h = mid - 1
            else:
                l = mid + 1

        return False
    
if __name__ == "__main__":
    obj = Solution()
    
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # target = 3

    matrix = [[1, 3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    
    ans = obj.searchMatrix(matrix, target)
    
    print(ans)
    