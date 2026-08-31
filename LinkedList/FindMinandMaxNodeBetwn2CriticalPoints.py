# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from CreateLinkedList import list_to_linkedlist, print_linkedlist


class Solution:
    def nodesBetweenCriticalPoints(self, head):
        points = []
        prev = head
        curr = head.next
        nxt = curr.next
        n = 1

        while nxt:
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                points.append(n)
            prev = curr
            curr = nxt
            nxt = nxt.next
            n += 1

        if len(points) < 2:
            return [-1, -1]

        mini = n
        for i in range(1, len(points)):
            mini = min(mini, points[i] - points[i-1])
        # print(points)

        return [mini, points[-1] - points[0]]


if __name__ == "__main__":
    arr = [1, 3, 2, 2, 3, 2, 2, 2, 7]
    head = list_to_linkedlist(arr)
    print_linkedlist(head)
    sol = Solution()
    print(sol.nodesBetweenCriticalPoints(head))