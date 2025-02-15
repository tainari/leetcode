class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def print_list(self):
        current = self.first
        vals = []
        while current:
            vals.append(current.value)
            current = current.next
        print(vals)

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return True

    def dequeue(self):
        if not self.first:
            return None
        node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            node.next = None
        self.length -= 1
        return node

queue = Queue(1)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_list()
queue.dequeue()
queue.print_list()
queue.dequeue()
queue.print_list()
queue.dequeue()
queue.print_list()
queue.dequeue()
queue.print_list()
queue.dequeue()
queue.print_list()
queue.enqueue(4)
queue.print_list()