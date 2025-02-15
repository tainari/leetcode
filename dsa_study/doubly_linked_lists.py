class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        current = self.head
        vals = []
        while current:
            vals.append(current.value)
            current = current.next
        print(vals)

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def traverse_list(self, index):
        if index >= self.length:
            return None
        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail
        # changing the method here a bit
        # and doing reverse indexing as in python lists
        # e.g., list[-1] = the last item.
        if index < 0:
            # so -1 = len(list) - 1
            # -2 = len(list) - 2 -- easy! :)
            old_index = index
            index = self.length + index
            # print(f"An index of {old_index} is the same as an index of {index}.")
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # [1, 2, 3, 4, 5]
            # index = 3; len = 5; last index = 4
            current = self.tail
            for ind in range(self.length - 1, index, -1):
                current = current.prev
        return current

    def get(self, index):
        if index >= self.length:
            return None
        node = self.traverse_list(index)
        return node.value

    def set_value(self, index, value):
        if index >= self.length:
            return None
        node = self.traverse_list(index)
        node.value = value
        return True

    def insert(self, value, index):
        if index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            next_node = self.traverse_list(index)
            prev_node = next_node.prev
            new_node.next = next_node
            new_node.prev = prev_node
            prev_node.next = new_node
            next_node.prev = new_node
            self.length += 1
        return True

    def remove(self, index):
        if index >= self.length:
            return None
        remove_node = self.traverse_list(index)
        prev_node = remove_node.prev
        next_node = remove_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        remove_node.next = None
        remove_node.prev = None
        self.length -= 1
        return remove_node


if __name__ == '__main__':
    ll = DoublyLinkedList(0)
    for val in range(1, 10):
        ll.append(val)
    ll.print_list()
    for ind in range(1, 10, 2):
        print(f"Inserting at index {ind}...")
        ll.insert(20 * (val + 1), index=ind)
        ll.print_list()
        print(f"Removing at index {ind}...")
        ll.remove(ind)
        ll.print_list()
        print("---")
    # for ind in range(0, ll.length):
    #     x = ll.get(ind)
    #     ll.set(ind, 20 * ind)
    #     y = ll.get(ind)
    #     print(f"{ind}: Old value = {x}; New value = {y}")
    # for ind in range(0, -ll.length, -1):
    #     x = ll.get(ind)
    #     ll.set(ind, 40 * ind)
    #     y = ll.get(ind)
    #     print(f"{ind}: Old value = {x}; New value = {y}")