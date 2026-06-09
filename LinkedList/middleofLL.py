"""
Leetcode Problem: 876
Desc: Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""
import CreateLinkedList

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    obj = Solution()

    l = [1, 2, 3, 4, 5]
    # l = [1, 2, 3, 4, 5, 6]
    head = CreateLinkedList.list_to_linkedlist(l)

    ans = obj.middleNode(head)
    CreateLinkedList.print_linkedlist(ans)

