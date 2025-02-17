class Heap:
    def __init__(self):
        self.heap = [None]

    def insert(self, item):
        self.heap.append(item)
        ind = len(self.heap) - 1
        parent_ind = ind // 2
        while parent_ind > 0 and self.heap[ind] > self.heap[parent_ind]:
            self.heap[ind], self.heap[parent_ind] = self.heap[parent_ind], self.heap[ind]
            ind = parent_ind
            parent_ind = ind // 2
        return True

    def _sink_down(self, ind):
        max_ind = ind
        while True:
            if ind * 2 < len(self.heap) and self.heap[max_ind] < self.heap[ind * 2]:
                max_ind = ind * 2
            if ind * 2 + 1 < len(self.heap) and self.heap[max_ind] < self.heap[ind * 2 + 1]:
                max_ind = ind * 2 + 1
            if ind == max_ind:
                return True
            self.heap[ind], self.heap[max_ind] = self.heap[max_ind], self.heap[ind]
            ind = max_ind

    def remove(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        removed_value = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._sink_down(1)
        return removed_value


myheap = Heap()
myheap.insert(1)
myheap.insert(-10)
myheap.insert(-15)

# myheap.insert(61)
# myheap.insert(58)

print(myheap.heap)

myheap.remove()
print(myheap.heap)

# myheap.insert(100)
#
# print(myheap.heap)
#
# myheap.insert(75)
#
# print(myheap.heap)
#
#
# heap = Heap()
# for i in [90, 75, 80, 55, 50, 65, 60]:
#     heap.add(i)
# print(heap.heap)
# heap.remove()
# print(heap.heap)

# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#
#     def _left_child(self, index):
#         return 2 * index + 1
#
#     def _right_child(self, index):
#         return 2 * index + 2
#
#     def _parent(self, index):
#         return (index - 1) // 2
#
#     def _swap(self, index1, index2):
#         self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
#
#     def insert(self, item):
#         self.heap.append(item)
#         ind = len(self.heap) - 1
#         parent_ind = (ind - 1) // 2
#         while parent_ind >= 0 and self.heap[ind] > self.heap[parent_ind]:
#             self.heap[ind], self.heap[parent_ind] = self.heap[parent_ind], self.heap[ind]
#             ind = parent_ind
#         return True
#
#
# myheap = MaxHeap()
# myheap.insert(99)
# myheap.insert(72)
# myheap.insert(61)
# myheap.insert(58)
#
# print(myheap.heap)
#
# myheap.insert(100)
#
# print(myheap.heap)
#
# myheap.insert(75)
#
# print(myheap.heap)
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     [99, 72, 61, 58]
#     [100, 99, 61, 58, 72]
#     [100, 99, 75, 58, 72, 61]
#
# """
