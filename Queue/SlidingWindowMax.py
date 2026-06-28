"""
Leetcode Problem: 239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is   moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.  

"""



from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        ans = []
        q = deque()

        for i in range(len(nums)):

            while q and q[0] <= i-k:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans


if __name__ == "__main__":
    obj = Solution()

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [1]
    # k = 1
    # nums = [1,-1]
    # k = 1

    ans = obj.maxSlidingWindow(nums, k)

    print(ans)