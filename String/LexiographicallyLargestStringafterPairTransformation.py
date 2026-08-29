'''
Leetcode Problem: 4036 Lexicographically Largest String After Pair Transformations
Description: You are given an array of integers nums. You can perform the following operation on nums any number of times:
- Choose any two elements nums[i] and nums[j] (i != j) and replace them with the sum of their values. The goal is to transform the array into a string by converting each integer into its corresponding lowercase letter (1 -> 'a', 2 -> 'b', ..., 26 -> 'z') and then concatenating them in any order. Return the lexicographically largest string that can be formed after performing the operations.
'''

class Solution:
    def largestString(self, nums):
        p = [1 << i for i in range(26)]
        ans = []

        for x in nums:
            temp = []

            count = x // p[25]
            temp.extend(['z'] * count)
            x %= p[25]

            for i in range(24, -1, -1):
                if p[i] <= x:
                    temp.append(chr(ord('a') + i))
                    x -= p[i]

            ans.append("".join(temp))

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    result = solution.largestString(nums)
    print(result) 