'''
Leetcode Problem : 33
Desc : Search for an element in rotated array in O(log n) time
'''

class Solution:
    def BSRotatedArray(self, nums, target):
        l = 0 
        r = len(nums)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
        
            if nums[mid] >= nums[l]:
                if nums[mid] > target and nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = r - 1
                    
        return -1
    

if __name__ == "__main__":
    
    # Example 1:
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0

    # Example 2:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3

    # Example 3:
    # nums = [1]
    # target = 0


    obj = Solution()
    ans = obj.BSRotatedArray(nums, target)
    
    print(ans)
                
            