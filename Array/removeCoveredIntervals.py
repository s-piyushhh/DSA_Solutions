"""
Leetcode Problem: 1288. Remove Covered Intervals
DEscription: Given a list of intervals, remove all intervals that are covered by another interval in the list. An interval [a,b) is covered by an interval [c,d) if and only if c <= a and b <= d. After doing so, return the number of remaining intervals.
"""
class Solution:
    def removeCoveredIntervals(self, intervals):
        removals = 0
        intervals.sort(key = lambda x : (x[0], -x[1]))

        lastMax = intervals[0][1]

        for i in intervals[1:]:
            if i[1] <= lastMax:
                removals += 1
            else:
                lastMax = i[1]
        
        return len(intervals)-removals
    

if __name__ == "__main__":
    intervals = [[1,4],[3,6],[2,8]]
    sol = Solution()
    print(sol.removeCoveredIntervals(intervals)) # Output: 2