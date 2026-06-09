"""
Leetcode Problem: 206
Desc: Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
import CreateLinkedList


class Solution:
    def reverseList(self, head): 
        last = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = last
            last = curr
            curr = nxt

        return last

if __name__ == "__main__":
    obj = Solution()
    
    l = [1, 2, 3, 4, 5]
    head = CreateLinkedList.list_to_linkedlist(l)
    
    # ans = obj.reverseList(head)
    # CreateLinkedList.print_linkedlist(ans)
    
    ans = CreateLinkedList.LL_to_list(obj.reverseList(head))
    print(ans)