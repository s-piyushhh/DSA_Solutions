"""
Leetcode Problem:3414
Description: You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.
"""

from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        # by right endpoint
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rights = [intervals[i][1] for i in order]

        prev = [(0, [])] * (n + 1)  # k = 0: nothing picked
        for _ in range(4):
            cur = [(0, [])] * (n + 1)
            for p in range(1, n + 1):
                i = order[p - 1]  # take next interval
                l, r, w = intervals[i]
                j = bisect_left(rights, l)  # intervals ending before l
                score, ids = prev[j]
                cur[p] = min((score - w, sorted(ids + [i])), cur[p - 1])
            prev = cur
        return prev[n][1]

if __name__ == "__main__":
    intervals = [[1, 3, 4], [2, 5, 2], [4, 6, 3], [7, 8, 5]]
    solution = Solution()
    result = solution.maximumWeight(intervals)
    print(result)  # Output: [0, 2, 3]