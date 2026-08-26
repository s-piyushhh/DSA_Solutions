'''
Leetcode Problem: Shortest and Lexicographically Smallest Beautiful String
Description: You are given a binary string s and a positive integer k.
A substring of s is beautiful if the number of 1's in it is exactly k.
Let len be the length of the shortest beautiful substring.
Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.
A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.
For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
'''

class Solution:
    def shortestBeautifulSubstring(self, s, k):
        ol = [] #ones locations
        for i in range(len(s)):
            if s[i] == '1':
                ol.append(i)

        ans = None

        for l in range(len(ol) - k + 1):
            temp = s[ol[l] : ol[l + k - 1] + 1]

            if ans is None:
                ans = temp
            elif len(temp) < len(ans):
                ans = temp
            elif len(temp) == len(ans):
                ans = min(ans, temp)

        return ans if ans is not None else ""
    
    
if __name__ == "__main__":
    s = "1101011"
    k = 3
    solution = Solution()
    result = solution.shortestBeautifulSubstring(s, k)
    print(result)