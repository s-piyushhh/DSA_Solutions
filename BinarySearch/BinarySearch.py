'''
Problem : LeetCode 704
Desc : Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
'''

class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums)
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

if __name__ == "__main__":
    # case1 :
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9
    
    # case2 :
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    obj = Solution()
    ans = obj.search(nums, target)
    
    print(ans)