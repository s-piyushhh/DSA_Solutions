'''
Desc: Given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. A single person can perform only one activity at a time, meaning no two activities can overlap. Your task is to determine the maximum number of activities that a person can complete in a day.

Note: Start time and finish time cannot overlap, i.e., if a person finishes an activity at time x, then they cannot start another activity at time x.

'''


class Solution:
    def activitySelection(self, start, finish):
        # code here
        l = list(zip(start, finish))
        l.sort(key=lambda x: x[1])

        last = l[0][1]

        ans = 1
        for i, j in l[1:]:
            if i > last:
                ans += 1
                last = j

        return ans


if __name__ == "__main__":

    obj = Solution()

    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]

    start = [10, 12, 20]
    # finish = [20, 25, 30]

    ans = obj.activitySelection(start, finish)

    print(ans)
