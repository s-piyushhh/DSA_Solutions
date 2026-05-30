"""
Leetcode Problem: 169

Desc: Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
if __name__ == "__main__":
    obj = Solution()
    
    # nums = [3, 2, 3]
    nums = [2, 2, 1, 1, 1, 2, 2]
    ans = obj.majorityElement(nums)
    print(ans)