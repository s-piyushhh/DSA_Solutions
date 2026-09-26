"""
Leetcode Problem: 1807. Evaluate the Bracket Pairs of a String
Description: You are given a string s that contains some bracket pairs, with each pair containing a non-empty key. You know the values of a wide range of keys. You are also given a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.
"""

class Solution:
    def evaluate(self, s, knowledge):
        m = {}
        for key in knowledge:
            m[key[0]] = key[1]

        i = 0
        n = len(s)
        ans = ""
        while i < n:
            if s[i] == "(":
                i += 1
                temp = ""
                while s[i] != ")":
                    temp += s[i]
                    i += 1

                if temp in m:
                    ans += m[temp]
                else:
                    ans += "?"

            else:
                ans += s[i]
            i += 1

        return ans

if __name__ == "__main__":
    s = "(name)is(age)yearsold"
    knowledge = [["name", "bob"], ["age", "two"]]
    
    solution = Solution()
    result = solution.evaluate(s, knowledge)
    print(result)