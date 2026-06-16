'''
Leetcode Problem : 455
Desc: Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        ans = 0
        j = 0
        for i in s:
            if i >= g[j]:
                ans += 1
                j += 1
            if j == len(g):
                break
        return ans


if __name__ == "__main__":

    obj = Solution()

    g = [1, 2, 3]
    s = [1, 1]
    
    g = [1, 2]
    # s = [1, 2, 3]

    ans = obj.findContentChildren(g, s)

    print(ans)
