"""
Leetcode Problem: 25
Desc : Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import CreateLinkedList

class Solution:
    def reverseKGroup(self, head, k):

        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        def rev(head, k):
            prev = None
            curr = head

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev, head, curr

        dummy = CreateLinkedList.ListNode(0)
        dummy.next = head

        group_prev = dummy
        curr = head

        for _ in range(n // k):
            new_head, new_tail, next_group = rev(curr, k)

            group_prev.next = new_head
            new_tail.next = next_group

            group_prev = new_tail
            curr = next_group

        return dummy.next


if __name__ == "__main__":
    obj = Solution()

    l = [1,2,3,4,5]
    k = 2
   
    # l = [1,2,3,4,5]
    # k = 3

    head = CreateLinkedList.list_to_linkedlist(l)

    ans = obj.reverseKGroup(head, k)
    CreateLinkedList.print_linkedlist(ans)
