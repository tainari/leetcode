class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        # print(f"Head is {self.head.value if self.head is not None else None}. Tail is {self.tail.value if self.tail is not None else None}. Length is {self.length}.")

    def get(self, index):
        if index < 0 or index >= self.length:
            print(f"Index invalid.")
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            # print(f"Got node {temp.value if temp is not None else None} at index {index}")
            return temp.value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print(f"Index invalid.")
            return
        curr = self.head
        prev = None
        for _ in range(index):
            prev = curr
            curr = curr.next
        new_node = Node(value)
        new_node.next = curr
        prev.next = new_node
        self.length += 1
        # print(f"Inserted node {value} at index {index}, between {prev.value} and {curr.value}. Length is {self.length}.")


    def pop(self):
        if self.head is None:
            pass
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            node = self.head
            prev = None
            while node.next is not None:
                prev = node
                node = node.next
            prev.next = None
            self.tail = prev
            self.length -= 1
        # print(f"Head is {self.head.value if self.head is not None else None}. Tail is {self.tail.value if self.tail is not None else None}. Length is {self.length}.")

    def pop_first(self):
        if self.head is None:
            pass
        else:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
        # print(f"Head is {self.head.value if self.head is not None else None}. Tail is {self.tail.value if self.tail is not None else None}. Length is {self.length}.")

    def prepend(self, value):
        # print(f"Old head value: {self.head.value} (length: {self.length})")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        # print(f"New head value: {self.head.value} (length: {self.length})")

    def print(self):
        list = []
        node = self.head
        while node is not None:
            list.append(node.value)
            node = node.next
        print(f"Current list: {list}")


    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.head
        curr = None
        for _ in range(index):
            curr = temp
            temp = temp.next
        curr.next = temp.next
        temp.next = None

    def reverse(self):
        if self.head is None:
            return None
        curr = self.head
        prev = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head, self.tail = self.tail, self.head


    def set_value(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.head
        for _ in range(index):
            temp = temp.next
        old_value = temp.value
        temp.value = value
        # print(f"Old value: {old_value}; new value: {temp.value}.")

if __name__ == '__main__':
    ll = LinkedList(0)
    for i in range(1,6):
        ll.append(i)
    ll.print()
    print(ll.get(index=4))
    ll.prepend(6)
    ll.print()
    ll.append(-1)
    ll.print()
    ll.insert(index=4, value=1000)
    ll.print()
    ll.remove(index=4)
    ll.print()
    ll.reverse()
    ll.print()
    ll.reverse()
    ll.print()
    # ll.append(2)
    # ll.append(3)
    # ll.prepend(4)
    # ll.prepend(5)
    # ll.get(4)
    # ll.set_value(index=4, value=1000)
    # ll.insert(index=4, value=0)
    # ll.pop()
    # ll.pop()
    # ll.pop_first()
    # ll.pop()
    # ll.pop()