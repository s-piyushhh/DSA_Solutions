"""
Leetcode Problem: 3517
Description: You are given a palindromic string s.
Return the lexicographically smallest palindromic permutation of s.
"""

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        m = {}

        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        m = dict(sorted(m.items()))

        middle = ""
        ans = []

        for i, j in m.items():
            if j % 2 != 0:
                middle = i

            n = 0
            while n < j // 2:
                ans.append(i)
                n += 1

        left = ans[:]

        if len(s) % 2 != 0:
            ans.append(middle)

        ans.extend(left[::-1])

        return "".join(ans)
    

if __name__ == "__main__":
    s = "aabb"
    solution = Solution()
    print(solution.smallestPalindrome(s))  # Output: "abba"