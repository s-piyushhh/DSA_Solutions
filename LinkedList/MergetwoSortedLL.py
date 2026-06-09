"""
Leetcode Problem: 21
Desc: You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

import CreateLinkedList


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = CreateLinkedList.ListNode(-1)
        curr = head

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return head.next


if __name__ == "__main__":
    obj = Solution()

    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    
    # list1 = []
    # list2 = [0]
    l1 = CreateLinkedList.list_to_linkedlist(list1)
    l2 = CreateLinkedList.list_to_linkedlist(list2)

    ans = obj.mergeTwoLists(l1, l2)
    CreateLinkedList.print_linkedlist(ans)
