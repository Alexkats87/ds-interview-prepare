"""
Classical Stack implementation
"""


class Stack:

    def __init__(self):
        self.data = []
        self.__size = 0
        self.__max_size = 10

    @property
    def size(self):
        return self.__size

    @property
    def max_size(self):
        return self.__max_size

    def show(self):
        print("Stack: ", self.data)

    def push(self, elem):
        if self.size == self.max_size:
            print("Stack full!")
        else:
            self.data.append(elem)
            self.__size += 1

    def pop(self):
        if self.size == 0:
            print("Stack is empty!")
            return None
        else:
            elem = self.data.pop()
            self.__size -= 1
            return elem


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(4)
    s.push(3)
    s.push(4)
    s.pop()
    s.show()