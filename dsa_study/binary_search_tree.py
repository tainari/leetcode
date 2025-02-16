class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        current = self.root
        while current:
            if value == current.value:
                return False
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return True
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return True
        return False

    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False


