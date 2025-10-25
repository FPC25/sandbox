class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_to_tail(self, node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node
        self._size += 1

    def remove_from_head(self):
        if self.is_empty():
            return None
        old = self.head
        self.head = old.next
        if self.head is None:
            self.tail = None
        old.set_next(None)
        self._size -= 1
        return old

    def peek_node(self):
        return self.head

    def enqueue(self, val):
        from node import Node
        self.add_to_tail(Node(val))

    def dequeue(self):
        node = self.remove_from_head()
        return None if node is None else node.val

    def peek(self):
        return None if self.head is None else self.head.val
    
