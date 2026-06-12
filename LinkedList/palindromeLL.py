"""
Leetcode Problem:234
Desc: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
import CreateLinkedList
class Solution:
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        def rev(curr):
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        revHead = rev(slow.next)

        first = head
        second = revHead

        while second:
            if first.val != second.val:
                slow.next = rev(revHead)
                return False
            first = first.next
            second = second.next

        slow.next = rev(revHead)
        return True


if __name__ == "__main__":
    obj = Solution()

    l = [1, 2, 2, 1]
    # l = [1, 2, 3, 4, 5, 6]
    head = CreateLinkedList.list_to_linkedlist(l)

    ans = obj.isPalindrome(head)
    print(ans)


# Find middle using slow/fast pointers.
# Reverse the second half.
# Compare first half and second half.
# Restore the list.
# Return result.
