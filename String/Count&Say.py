"""
Leetcode Problem 38: Count and Say
Description:
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

"""

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        ans = '1'
        for i in range(1, n):
            count = 1
            temp = ""
            for i in range(len(ans)-1):
                if ans[i] != ans[i+1]:
                    temp += str(count) + ans[i]
                    count = 1
                else:
                    count += 1
            temp += str(count) + ans[-1]
            ans = temp

        return ans


if __name__ == "__main__":
    n = 5
    solution = Solution()
    result = solution.countAndSay(n)
    print(result)  # Output: "111221"