"""
Description: Given an integer array nums and an integer k, return an array of the number of distinct elements in every subarray of size k.
"""


class Solution:
    def distinctNumbers(self, nums, k):
        # Your code goes here
        m = {}
        for i in nums[:k]:
            m[i] = m.get(i, 0)+1

        ans = [len(m)]
        for idx, i in enumerate(nums[k:]):
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

            m[nums[idx]] -= 1
            if m[nums[idx]] == 0:
                del m[nums[idx]]

            ans.append(len(m))

        return ans

if __name__ == "__main__":
    nums = [1, 2, 3, 2, 1]
    k = 3
    solution = Solution()
    print(solution.distinctNumbers(nums, k))  # Output: [3, 3, 2]