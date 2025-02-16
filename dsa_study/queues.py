class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:
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

my_queue = MyQueue(1)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.dequeue()
my_queue.print_list()
my_queue.enqueue(4)
my_queue.print_list()