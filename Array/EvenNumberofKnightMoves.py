"""
Leetcode Problem: 3996
Description:
You are given two integer arrays start and target, both of length 2, representing the coordinates of a knight on an infinite chessboard. The knight can move in an "L" shape: two squares in one direction and then one square perpendicular to that, or one square in one direction and then two squares perpendicular to that.
Return true if it is possible for the knight to reach the target position from the start position in an even number of moves, or false otherwise.
"""

class Solution:
    def canReach(self, start, target):
        return abs(target[0] - start[0]) % 2 == abs(target[1] - start[1]) % 2
    
if __name__ == "__main__":
    solution = Solution()
    start = [0, 0]
    target = [2, 1]
    print(solution.canReach(start, target))  # Output: True

    start = [0, 0]
    target = [1, 2]
    print(solution.canReach(start, target))  # Output: True

    start = [0, 0]
    target = [1, 1]
    print(solution.canReach(start, target))  # Output: False