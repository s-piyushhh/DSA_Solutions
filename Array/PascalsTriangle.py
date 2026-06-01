'''
Leetcode Problem: 118
Desc: Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''


class Solution:
    def generate(self, n):
        ans = [[1], [1, 1]]
        for i in range(2, n):
            temp = [1]
            for j in range(1, i):
                temp.append(ans[i-1][j-1] + ans[i-1][j])
            temp.append(1)
            ans.append(temp)
        return ans[:n]




if __name__ == "__main__":
    obj = Solution()
    
    # n = 6
    n = 3
    # n = 1
    ans = obj.generate(n)
    print(ans)
