class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if self.value >= value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if self.value == value:
            return True
        elif self.value >= value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.find(value)

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.value)
        if self.right is not None:
            self.right.printInOrder()


def array_to_bst(arr):
    if not arr:
        return None
    root = Node(arr[0])

    for value in arr[1:]:
        root.insert(value)
    return root


def main():
    arr = [10, 5, 15, 3, 7, 12, 20]
    bst = array_to_bst(arr)
    bst.printInOrder()


main()
