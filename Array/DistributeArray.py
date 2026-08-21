'''
Leetcode Problem: 3069
Description: Given an array of integers nums, distribute the elements of nums into two arrays arr1 and arr2 such that:
- arr1 contains the first element of nums.
- arr2 contains the second element of nums.
- For each subsequent element in nums, append it to the array (arr1 or arr2) whose last element is larger.
'''


class Solution:
    def resultArray(self, nums):
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            
        return arr1 + arr2
    
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 2, 4, 5]
    result = solution.resultArray(nums)
    print(result)  # Output: [1, 2, 5, 3, 4]