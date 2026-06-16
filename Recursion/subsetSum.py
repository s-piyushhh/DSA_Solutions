"""
Desc: Given an array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.
"""


class Solution:
    def subsetSums(self, arr):
        ans = []
        def helper(i, tot):
            if i == len(arr):
                ans.append(tot)
                return 
            helper(i+1, tot+ arr[i])
            helper(i+1, tot)
        helper(0, 0)
        return ans
 
if __name__ == "__main__":
    obj = Solution()
    
    # arr = [2, 3]
    # arr = [1, 2, 1]
    arr = [5, 6, 7]
    ans = obj.subsetSums(arr)
    print(ans)



