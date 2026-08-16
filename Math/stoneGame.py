'''
Leetcode Problem: 2029. Stone Game IX
Description:
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stones. 

'''



class Solution:
    def stoneGameIX(self, stones):
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            if (typ := val % 3) == 0:
                cnt0 += 1
            elif typ == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2
    

if __name__ == "__main__":
    stones = [2, 1]
    solution = Solution()
    result = solution.stoneGameIX(stones)
    print(result)  # Output: True