"""
Leetcode Problem: 836. Rectangle Overlap
Description: An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner. Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
"""

class Solution:
    def isRectangleOverlap(self, *A):
        (x1, y1, x2, y2), (X1, Y1, X2, Y2) = A
        return x1 < X2 and X1 < x2 and y1 < Y2 and Y1 < y2
    
if __name__ == "__main__":
    solution = Solution()
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    print(solution.isRectangleOverlap(rec1, rec2))  # Output: True