'''
Leetcode Problem: 2089. Find Target Indices After Sorting Array
Description: Given a 0-indexed integer array nums and a target element target, return a list of the target's indices after sorting nums in non-decreasing order. If the target is not in nums, return an empty list. You must write an algorithm with O(n) runtime complexity.
'''

class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 5, 2, 3]
    target = 2
    print(solution.targetIndices(nums, target))  # Output: [1, 2]