'''
Leetcode 139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
'''

from collections import deque 
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.wordBreak("leetcode", ["leet", "code"]))  # Output: True
    print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
    print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False