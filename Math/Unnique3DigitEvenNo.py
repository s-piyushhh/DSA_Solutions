"""
Leetcode Problem: 3483
Description:You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
Note: Each copy of a digit can only be used once per number, and there may not be leading zeros. 
"""

from itertools import permutations    
class Solution:
    def totalNumbers(self, digits):
        numbers = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                numbers.add((a, b, c))
        
        # print(numbers)

        return len(numbers)
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.totalNumbers([2, 1, 3, 0]))
    print(solution.totalNumbers([2, 2, 8, 8, 2]))
    print(solution.totalNumbers([3, 7, 5]))
    
    
