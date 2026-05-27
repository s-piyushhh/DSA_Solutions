"""
LeetCode Problem : 3121
Desc: You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.
"""


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        m = {}
        for i in range(len(word)-1, -1, -1):
            if word[i].islower() and word[i] not in m:
                m[word[i]] = i
        # print(m)
        ans = 0
        checked = set()
        for i, c in enumerate(word):
            if c.isupper() and c.lower() in m and c not in checked:
                checked.add(c)
                if m[c.lower()] > i:
                    continue
                ans += 1
        return ans
    
if __name__ == "__main__":
    obj = Solution()
    
    word = "aaAbcBC"
    # word = "abc"
    # word = "AbBCab"

    ans = obj.numberOfSpecialChars(word)
    
    print(ans)