""""
Leetcode Problem: 56
Desc :Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)-1):
            end = max(end, intervals[i][1])
            if end < intervals[i+1][0]:
                ans.append([start, end])
                start = intervals[i+1][0]
                end = intervals[i+1][1]

        if end < intervals[-1][1]:
            end = intervals[-1][-1]
        ans.append([start, end])
        return ans


if __name__ == "__main__":
    obj = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]    
    # intervals = [[4, 7], [1, 4]]
    
    ans = obj.merge(intervals)
    print(ans)
