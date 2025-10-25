class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.items:
           return None
        return self.items[-1]
    
    def pop(self):
        if not self.items:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item 