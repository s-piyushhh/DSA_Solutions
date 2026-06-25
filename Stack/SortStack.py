"""
Desc: Given a stack of integers st[]. Sort the stack in ascending order (smallest element at the bottom and largest at the top).

Examples:

Input: st[] = [41, 3, 32, 2, 11]
Output: [41, 32, 11, 3, 2]
Explanation: After sorting, the smallest element (2) is at the bottom and the largest element (41) is at the top.
"""



class Solution:
    def sortStack(self, st):
        if not st:
            return

        temp = st.pop()
        self.sortStack(st)
        self.sortedInsert(st, temp)

    def sortedInsert(self, stack, x):
        if not stack or stack[-1] <= x:
            stack.append(x)
            return

        temp = stack.pop()
        self.sortedInsert(stack, x)
        stack.append(temp)


if __name__ == "__main__":
    obj = Solution()

    st = [41, 3, 32, 2, 11]

    obj.sortStack(st)
    print(st)
