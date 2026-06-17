"""
Leetcode Problem: 39
Desc: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


class Solution:
    def combinationSum(self, c, target):
        ans = []

        def helper(i, tot, temp):
            if tot == target:
                ans.append(temp.copy())
                return

            if i == len(c) or tot > target:
                return

            temp.append(c[i])
            helper(i, tot + c[i], temp)
            temp.pop()

            helper(i+1, tot, temp)

            return

        helper(0, 0, [])

        return ans


if __name__ == "__main__":
    obj = Solution()

    # candidates = [2, 3, 6, 7]
    # target = 7
    
    candidates = [2, 3, 5]
    target = 8

    ans = obj.combinationSum(candidates, target)
    print(ans)
