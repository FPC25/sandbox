class MinHeap:
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
    def peek_min(self):
        if not self.heap:
            raise IndexError("can't peek_min from an empty heap")
        return self.heap[0]

    # O(log n) time complexity
    def extract_min(self):
        if not self.heap:
            raise IndexError("can't extract_min from an empty heap")
        min_element = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        return min_element

    # O(n) time complexity
    def heapify(self, elements):
        #turn a list into a heap
        if not elements:
            self.heap = []
        else:
            self.heap = list(elements)
            for i in reversed(range((self._parent(len(self.heap) - 1) or 0) + 1)):
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
        return (index - 1) // 2 if index > 0 else None
    
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
        #swin operation
        parent_index = self._parent(index)
        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    # O(log n) time complexity
    def _sift_down(self, index):
        #sink operation
        while True:
            smallest = index
            left_child = self._left_child(index)
            right_child = self._right_child(index)
            

            if left_child is not None and self.heap[left_child][0] < self.heap[smallest][0]:
                smallest = left_child
                
            if right_child is not None and self.heap[right_child][0] < self.heap[smallest][0]:
                smallest = right_child
                
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
            
if __name__ == "__main__":
    
    min_heap = MinHeap()
    min_heap.heapify([[10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']])
    print("Heap after heapify:", min_heap)
    
    import heapq
    mylist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(mylist)
    print("Heap using heapq:", mylist)
    
    print(min_heap.extract_min())  # Should return (1, '1')
    print(min_heap.extract_min())  # Should return (2, '2')
    print(min_heap.extract_min())  # Should return (3, '3')
    
    print(heapq.heappop(mylist))  # Should return 1
    print(heapq.heappop(mylist))  # Should return 2
    print(heapq.heappop(mylist))  # Should return 3
    
    min_heap.insert(2, '2')
    print("Heap after inserting (2, '2'):", min_heap)
    
    heapq.heappush(mylist, 2)
    print("Heap using heapq after pushing 2:", mylist)
    
    
    min_heap2 = MinHeap()
    min_heap2.heapify([[5, '5'], [7, '7'], [2, '2']])
    min_heap.meld(min_heap2)
    print("Heap after melding with another heap:", min_heap)
    
    
