'''
Leetcode Problem: Minimum Bishop Moves to Reach Target

Description : There is an 8 x 8 empty chessboard with 1-indexed rows and columns.
You are given an array source = [sr, sc] representing the starting position of a bishop, and an array target = [tr, tc] representing the target position. In one move, the bishop travels one or more squares along a single diagonal direction, staying within the board.

Return the minimum number of moves for the bishop to land exactly on target. If it can never reach target, return -1.
'''

from ast import If


class Solution:
    def minBishopMoves(self, source, target):
        if abs(source[0] - source[1]) % 2 != abs(target[0] - target[1]) % 2:
            return -1

        if abs(source[0] - target[0]) == abs(source[1] - target[1]):
            return 1

        return 2


if __name__ == "__main__":
    solution = Solution()
    source = [1, 1]
    target = [8, 8]
    print(solution.minBishopMoves(source, target))  # Output: 1