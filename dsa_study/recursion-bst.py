class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __print_tree(self, current_node):
        ans = []
        if current_node:
            print(f"Adding {current_node.value}...")
            ans.append(current_node.value)
            if current_node.left:
                ans.extend(self.__print_tree(current_node.left))
            if current_node.right:
                ans.extend(self.__print_tree(current_node.right))
        return ans

    def print_tree(self):
        ans = self.__print_tree(self.root)
        print(ans)

    def __get(self, value, current_node):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if current_node.value < value:
            self.__get(value, current_node.left)
        if current_node.value > value:
            self.__get(value, current_node.right)

    def get(self, value):
        return self.__get(value)

    def __insert(self, value, current_node):
        if not current_node:
            return Node(value)
        if value < current_node.value:
            print(f"Percolating {value} left of {current_node.value}")
            current_node.left = self.__insert(value, current_node.left)
        if value > current_node.value:
            print(f"Percolating {value} right of {current_node.value}")
            current_node.right = self.__insert(value, current_node.right)
        return current_node

    def insert(self, value):
        print(f"Inserting {value}...")
        node = self.__insert(value, self.root)
        if not self.root:
            self.root = node


bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(9)
bst.insert(8)
bst.insert(7)
bst.insert(6)
bst.insert(10)
bst.print_tree()