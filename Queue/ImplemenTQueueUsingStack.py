"""
Leetcode Problem: Implement Queue using Stacks
Description:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
"""


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = [] 

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.transfer()
        return self.s2.pop()

    def peek(self) -> int:
        self.transfer()
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0

    def transfer(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == "__main__":
    # Example usage
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # returns 1
    print(queue.pop())   # returns 1
    print(queue.empty()) # returns False