"""
Binary tree (v.2) implementation

A lot of extra methods presented
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)

        # If root is None, assign the new node to the root
        if self.root is None:
            self.root = new_node

        else:
            focus_node = self.root
            parent = None

            while True:
                parent = focus_node

                # If data is less than focus_node, assign focus_node to the left child
                if data < focus_node.data:
                    focus_node = focus_node.left

                    # If there's no left child, assign the new node to the left child
                    if focus_node is None:
                        parent.left = new_node
                        return

                else:
                    focus_node = focus_node.right

                    # If there's no right child, assign the new node to the right child
                    if focus_node is None:
                        parent.right = new_node
                        return

    # ================== Functions ===============================
    # ============================================================

    # 1. Traverse

    # 1.1 DFS

    #  Inorder traversal gives nodes in non-decreasing order.
    #  We visit the left child first, then the root, and then the right child.
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    # Preorder traversal first visits the root node and then traverses the left and the right subtree.
    # It is used to create a copy of the tree.
    def pre_order_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # Postorder traversal first traverses the left and the right subtree and then visits the root node.
    # It is used to delete the tree.
    def post_order_traversal(self, node):
        if node is not None:
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
            print(node.data, end=" ")

    # 1.2 BFS

    @staticmethod
    def bfs(node):
        # Base Case
        if node is None:
            return

        # Create an empty queue for level order traversal
        queue = [node]

        # Enqueue Root and initialize height
        while len(queue) > 0:

            # Print front of queue and
            # remove it from queue
            print(queue[0].data, end=" ")
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

    # 1.3 Selected level

    # Print nodes at a given level
    def print_given_level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data, end=" ")
        elif level > 1:

            self.print_given_level(node.left, level - 1)
            self.print_given_level(node.right, level - 1)

    # Print tree level wise
    def print_level_order(self, root):
        h = self.height
        for i in range(1, h + 1):
            self.print_given_level(root, i)
            print()

    # ============================================================
    # 2. Counters

    # 2.1 Tree size
    @property
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    # 2.2 Height of the BST
    @property
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            # Compute the depth of each subtree
            l_depth = self._height(node.left)  #
            r_depth = self._height(node.right)  #

            # Use the larger one
            if l_depth > r_depth:
                return l_depth + 1
            else:
                return r_depth + 1

    # =============================================================
    # 3. Modifiers

    # 3.1 Delete node

    # Function that returns the node with minimum key value found in that tree
    @staticmethod
    def min_value_node(node):
        current = node

        # Loop down to find the leftmost leaf
        while current and current.left is not None:
            current = current.left

        return current

    # Function that deletes the key and returns the new root
    def delete_node(self, root, key):
        # base Case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in left subtree
        if key < root.key:
            root.left = self.delete_node(root.left, key)

        # If the key to be deleted is greater than the root's key, then it lies in right subtree
        elif key > root.key:

            root.right = self.delete_node(root.right, key)

        # If key is same as root's key, then this is the node to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor(smallest in the right subtree)
            temp = self.min_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.delete_node(root.right, temp.key)

        return root

    # Find inorder successor: min(x: x > input)
    def find_inorder(self, inp):

        res = None

        if self.root is None:
            return res

        res = self.root.data

        for node in self._find_inorder(self.root):
            elem = node.data
            print(elem)
            if elem:
                if inp < elem < res:
                    res = elem

        print(f"{res=}")

    # Inorder traverse with yielding values
    def _find_inorder(self, node):

        if node:
            for el in self._find_inorder(node.left):
                yield el
            yield node
            for el in self._find_inorder(node.right):
                yield el


if __name__ == '__main__':

    tree = BinaryTree()
    tree.add_node(50)
    tree.add_node(25)
    tree.add_node(75)
    tree.add_node(12)
    tree.add_node(37)
    tree.add_node(43)
    tree.add_node(30)

    tree.bfs(tree.root)

    # tree.pre_order_traversal(tree.root)
    # print()
    # tree.in_order_traversal(tree.root)
    # print()
    # tree.post_order_traversal(tree.root)
    # print()
    # print(tree.height)
    # print()
    # tree.print_given_level(tree.root, 2)
    # print()
    # print()
    # tree.print_level_order(tree.root)
    # print()
    # print(tree.size)

    # print(tree.find_inorder(29))

