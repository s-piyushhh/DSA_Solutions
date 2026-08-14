'''
Leetcode 3090: Maximum Length of Substring With at Most Two Occurrences
Description: Given a string s, return the length of the longest substring that contains at most two occurence of a character.
'''

class Solution:
    def maximumLengthSubstring(self, s):
        m = {}
        l = 0
        r = 0
        ans = 0
        while l <= r and r < len(s):
            if s[r] in m:
                m[s[r]] += 1
            else:
                m[s[r]] = 1

            while m[s[r]] > 2:
                m[s[l]] -= 1
                l += 1

            ans = max(ans, r - l+1)
            r += 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "bcbbbcba"
    result = solution.maximumLengthSubstring(s)
    print(f"The length of the longest substring with at most two occurrences in the string '{s}' is: {result}")