class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linkedlist(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
    
def LL_to_list(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l
