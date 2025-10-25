class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)
    
    def __repr__(self):
        return str(self.heap)

    # O(log n) time complexity
    def insert(self, key, value):
        self.heap.append([key, value])
        self._sift_up(len(self.heap) - 1)

    # O(1) time complexity
    def peek_max(self):
        if not self.heap:
            raise IndexError("can't peek_max from an empty heap")
        return self.heap[0]

    # O(log n) time complexity
    def extract_max(self):
        if not self.heap:
            raise IndexError("can't extract_max from an empty heap")
        max_element = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        return max_element

    # O(n) time complexity
    def heapify(self, elements):
        #turn a list into a heap
        if not elements:
            self.heap = []
        else:
            self.heap = list(elements)
            for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
                self._sift_down(i) 

    # O(n) time complexity
    def meld(self, other_heap):
        # Ensure both heaps are valid lists
        self.heap = self.heap if self.heap is not None else []
        other_heap.heap = other_heap.heap if other_heap.heap is not None else []
        
        #combine two heaps
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)
        
        other_heap.heap = []  # Clear the other heap

    # O(1) time complexity
    def _parent(self, index):
        return (index - 1) // 2 if index > 0 else 0
    
    # O(1) time complexity
    def _left_child(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None
    
    # O(1) time complexity
    def _right_child(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    # O(log n) time complexity
    def _sift_up(self, index):
        #sift_up or swim operation
        parent_index = self._parent(index)
        while parent_index is not None and self.heap[index][0] > self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    # O(log n) time complexity
    def _sift_down(self, index):
        #sink operation
        while True:
            largest = index
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            if left_child is not None and left_child < len(self.heap) and self.heap[left_child][0] > self.heap[largest][0]:
                largest = left_child

            if right_child is not None and self.heap[right_child][0] > self.heap[largest][0]:
                largest = right_child

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
            largest = left_child

            if right_child is not None and self.heap[right_child][0] > self.heap[largest][0]:
                largest = right_child

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10, "A")
    max_heap.insert(20, "B")
    max_heap.insert(15, "C")
    print("Heap after inserts:", max_heap)

    print("Max element:", max_heap.peek_max())

    print("Extracted max:", max_heap.extract_max())
    print("Heap after extraction:", max_heap)

    other_heap = MaxHeap()
    other_heap.insert(25, "D")
    other_heap.insert(5, "E")
    print("Other heap:", other_heap)

    max_heap.meld(other_heap)
    print("Heap after melding:", max_heap)
    print("Other heap after melding (should be empty):", other_heap)