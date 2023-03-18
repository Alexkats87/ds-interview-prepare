"""
Linked list implementation
"""


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def sorted_insert(self, new_node):

        # Special case for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:

            # Locate the node before the point of insertion
            current = self.head
            while (current.next is not None and
                   current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        temp = self.head
        prev = self.head
        if temp.data == data:
            if temp.next is None:
                print("Can't delete the node as it has only one node")
            else:
                temp.data = temp.next.data
                temp.next = temp.next.next
            return
        while temp.next is not None and temp.data != data:
            prev = temp
            temp = temp.next
        if temp.next is None and temp.data != data:
            print("Can't delete the node as it doesn't exist")

        # If node is last node of the linked list
        elif temp.next is None and temp.data == data:
            prev.next = None
        else:
            prev.next = temp.next

    # Utility function to print it the LinkedList
    def print_list(self):
        elems = ""
        temp = self.head
        while temp:
            elems = elems + f"{temp.data} -> "
            temp = temp.next
        print(elems[:-3])


if __name__ == "__main__":

    llist = LinkedList()
    node = Node(5)
    llist.sorted_insert(node)
    node = Node(10)
    llist.sorted_insert(node)
    node = Node(7)
    llist.sorted_insert(node)
    node = Node(3)
    llist.sorted_insert(node)
    node = Node(1)
    llist.sorted_insert(node)
    node = Node(9)
    llist.sorted_insert(node)
    print("Create Linked List")
    llist.print_list()

    print("Delete node 5")
    llist.delete_node(5)
    print("Linked List after deletion")
    llist.print_list()
