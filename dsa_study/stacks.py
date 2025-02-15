class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1

    def print_list(self):
        current = self.top
        vals = []
        while current:
            vals.append(current.value)
            current = current.next
        print(vals)

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        node = self.top
        if self.height == 1:
            self.top = None
        else:
            node = self.top
            self.top = self.top.next
        node.next = None
        self.height -= 1
        return node


if __name__ == '__main__':
    stack = Stack(5)
    stack.print_list()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_list()
    stack.pop()
    stack.print_list()
    stack.pop()
    stack.print_list()