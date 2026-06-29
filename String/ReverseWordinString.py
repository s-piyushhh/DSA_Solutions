"""
Leetcode Problem: 151. Reverse Words in a String    
Description: Given an input string s, reverse the order of the words.
"""



class Solution:
    def reverseWords(self, s):
        ans = []
        temp = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                temp += s[i]
            elif temp:
                ans.append(temp[::-1])
                temp = ""

        if temp:
            ans.append(temp[::-1])

        return " ".join(ans)

if __name__ == "__main__":
    s = "the sky is blue"
    solution = Solution()
    print(solution.reverseWords(s))  # Output: "blue is sky the"    