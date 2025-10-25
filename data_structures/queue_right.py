# Queue head to the right
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.appendleft(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)