"""
Leetcode Problem: 436
Desc: You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
"""


class Solution:
    def solve(self, intervals):
        si = []  # start Intervals
        m = {}
        n = len(intervals)

        for i, x in enumerate(intervals):
            m[x[0]] = i
            si.append(x[0])

        si.sort()
        ans = []
        for i, x in enumerate(intervals):
            l = 0
            r = n - 1
            temp = -1
            while l <= r:
                mid = l + (r-l)//2
                if si[mid] >= x[1]:
                    temp = m[si[mid]]
                    r = mid - 1
                else:
                    l = mid + 1
            ans.append(temp)

        return ans

if __name__ == "__main__":
    obj = Solution()
    
    # intervals = [[1, 2]]
    # intervals = [[3, 4],[2,3],[1,2]]
    intervals = [[1, 4],[2,3],[3,4]]
    
    ans = obj.solve(intervals)
    print(ans)