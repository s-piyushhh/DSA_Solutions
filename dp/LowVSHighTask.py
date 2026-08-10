'''
GFG Problem: High Effort vs Low Effort Task
Description: Given two arrays h and l of size n, where h[i] is the high effort task and l[i] is the low effort task. You have to choose either high effort or low effort task for each day such that you cannot choose high effort task on two consecutive days. Find the maximum total effort you can achieve.
'''


class Solution:
    def maxTask(self, h, l):
        # code here
        prevprev = 0
        prev = max(h[0], l[0])
        curr = prev
        
        for i in range(1, len(h)):
            curr = max(h[i] + prevprev, l[i] + prev)
            prevprev = prev
            prev = curr
            
        
        return curr
    
if __name__ == "__main__":
    h = [10, 5, 15, 20]
    l = [5, 10, 5, 10]
    solution = Solution()
    print(solution.maxTask(h, l))  # Output: 40