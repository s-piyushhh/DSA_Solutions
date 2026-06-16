'''
Desc: Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''


class Solution:
    def subsetsWithDup(self, nums):

        nums.sort()
        ans = []

        def helper(idx, temp):

            ans.append(temp[:])

            for i in range(idx, len(nums)):

                if i > idx and nums[i] == nums[i - 1]:
                    continue

                temp.append(nums[i])

                helper(i + 1, temp)

                temp.pop()

        helper(0, [])

        return ans


if __name__ == "__main__":
    obj = Solution()

    arr = [1, 2, 2]

    ans = obj.subsetsWithDup(arr)
    print(ans)
