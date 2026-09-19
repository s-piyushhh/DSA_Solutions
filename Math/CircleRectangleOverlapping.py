"""
Leetcode Problem: 1401. Circle and Rectangle Overlapping
Description: Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle. Return true if the circle and rectangle are overlapped otherwise return false.
"""


class Solution:
    def checkOverlap(self, r, cx, cy, x1, y1, x2, y2) -> bool:
        x = max(x1, min(cx, x2)) - cx
        y = max(y1, min(cy, y2)) - cy

        return x * x + y * y <= r * r

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkOverlap(1, 0, 0, 1, -1, 3, 1))  # Output: True
    print(solution.checkOverlap(1, 0, 0, -1, -1, 0, 1))  # Output: True
    print(solution.checkOverlap(1, 0, 0, 1, 1, 2, 2))    # Output: False