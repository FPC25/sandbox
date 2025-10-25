# Queue head to the left
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.popleft()

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)