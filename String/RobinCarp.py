"""
Leetcode Problem: 686. Repeated String Match
Description: Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.
"""

class Solution:
    def repeatedStringMatch(self, a, b):
        ans = (len(a) + len(b) - 1) // len(a)
        s = a * ans

        if b in s:
            return ans
        s += a
        if b in s:
            return ans + 1
        
        return -1
        
if __name__ == "__main__":
    a = "abcd"
    b = "cdabcdab"
    solution = Solution()
    print(solution.repeatedStringMatch(a, b))  # Output: 3  