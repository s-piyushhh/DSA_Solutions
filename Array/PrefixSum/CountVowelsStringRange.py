"""
Leetcode Problem: 2559. Count Vowel Strings in Ranges
Description: Given an array of strings words and an array of queries where queries[i] = [li, ri], return an array of integers answer, where answer[i] is the number of strings in words[li...ri] (inclusive) that start and end with a vowel.
"""


class Solution:
    def vowelStrings(self, words, queries): 
        pref = []
        tot = 0
        vowels = {'a', 'e', 'o', 'i', 'u'}
        for i in words:
            pref.append(tot)
            if i[0] in vowels and i[-1] in vowels:
                tot += 1

        pref.append(tot)

        ans = []
        for i in queries:
            curr = pref[i[-1]+1] - pref[i[0]]
            # if words[i[0]][0] in vowels and words[i[0]][-1] in vowels:
            #     curr += 1

            ans.append(curr)

        return ans
if __name__ == "__main__":
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]]
    solution = Solution()
    print(solution.vowelStrings(words, queries))  # Output: [2, 3, 0]