"""
Binary tree (v.1) implementation
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
            print(self.data),
        if self.right:
            self.right.print_tree()
            print(self.data)


if __name__ == '__main__':
    t = Node(1)
    t.insert(2)
    t.insert(3)
    t.insert(4)
    t.insert(5)

    t.print_tree()


