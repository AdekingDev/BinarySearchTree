class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, value):
        if value not in self.heap:
            print(f"{value} not found in the heap.")
            return

        index = self.heap.index(value)
        self.heap[index] = self.heap[-1]
        del self.heap[-1]

        if index < len(self.heap):
            self._heapify_down(index)

    def _heapify_up(self, index):
        parent_index = (index - 1)
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Use case
heap = MinHeap()
elements = [15, 40, 30, 50, 10, 100, 40]

for element in elements:
    heap.insert(element)

print("Heap elements after insertion:", heap.heap)
visited_elements = []
while heap.heap[0] != 40:
    visited_elements.append(heap.heap[0])
    heap.delete(heap.heap[0])

print("Elements visited before finding 40:", visited_elements)
heap.delete(10)
print("Heap elements after deleting 10:", heap.heap)
