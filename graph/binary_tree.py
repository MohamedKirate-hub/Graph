class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = Node(value)
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = Node(value)
                return
            else:
                queue.append(current.right)

    def print_nodes(self):
        start = self.root
        if start is None:
            return
        queue = [start]
        while queue:
            current = queue.pop(0)
            print(current.value)
            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)


def main():
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(14)
    tree.insert(19)
    tree.insert(26)
    tree.insert(27)
    tree.insert(31)
    tree.insert(33)
    tree.insert(35)
    tree.insert(42)
    tree.insert(44)

    tree.print_nodes()


main()
