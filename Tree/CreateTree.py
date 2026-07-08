from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(arr):
    if not arr or arr[0] is None:
        return None

    root = Node(arr[0])
    q = deque([root])

    i = 1

    while q and i < len(arr):
        curr = q.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1

    return root


def display(root, level=0, prefix="Root: "):
    if root is None:
        return

    print(" " * (4 * level) + prefix + str(root.data))
    display(root.left, level + 1, "L--- ")
    display(root.right, level + 1, "R--- ")

arr = [1, 2, 3, 4, 5, None, 7]

root = buildTree(arr)
display(root)
