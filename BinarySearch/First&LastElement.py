"""
LeetCode Problem: 34
Desc : Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
"""

class Solution:
    def Solve(self, nums, target):
        #for first occurence of target
        l = 0
        r = len(nums) - 1
        first = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        # for last occurence of target
        l = 0
        r = len(nums) - 1
        last = first
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                last = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return [first, last]
    

if __name__ == "__main__":
    obj = Solution()
    
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    
    nums = [5, 6, 7, 7, 8, 8, 10]
    target = 6
    # nums = []
    # target = 0
    
    ans = obj.Solve(nums, target)
    
    print(ans)
                
