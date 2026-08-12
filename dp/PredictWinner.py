'''
Leetcode Problem: 486. Predict the Winner
Description: You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
The players take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.
'''


class Solution:
    def predictTheWinner(self, nums):
        m = {}

        def search(l, r):
            if l == r:
                return nums[l]

            if (l, r) in m:
                return m[(l, r)]
            
            take_left = nums[l] - search(l+1, r)
            take_right = nums[r] - search(l, r-1)

            m[(l,r)] = max(take_left, take_right)

            return m[(l, r)]

        return search(0, len(nums)-1) >= 0  

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 2]
    nums2 = [1, 5, 233, 7]
    nums3 = [1, 3, 7, 8]
    print(sol.predictTheWinner(nums2))  # Output: True
    print(sol.predictTheWinner(nums))  # Output: False
    print(sol.predictTheWinner(nums3))  # Output: True