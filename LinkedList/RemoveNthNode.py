"""
Leetcode Probleem : 19
Desc: Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
import CreateLinkedList

class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next

        if l == n:
            return head.next

        temp = head
        prev = None
        curr = 0
        while temp:
            curr += 1
            if curr == l - n + 1:
                prev.next = temp.next
                return head
            prev = temp
            temp = temp.next

        return head


if __name__ == "__main__":
    obj = Solution()

    l = [1,2,3,4,5]
    n = 2
    
    # head = [1, 2]
    # n = 1
    
    head = CreateLinkedList.list_to_linkedlist(l)

    ans = obj.removeNthFromEnd(head, n)
    CreateLinkedList.print_linkedlist(ans)
