"""
Leetcode Problem: 3
Desc: Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        l = []
        for i in s:
            if i not in l:
                l.append(i)
            elif i in l:
                x = l.index(i)
                del l[:x+1]
                l.append(i)
            maxi = max(maxi, len(l))
        return maxi


if __name__ == "__main__":
    obj = Solution()

    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"

    ans = obj.lengthOfLongestSubstring(s)
    print(ans)
