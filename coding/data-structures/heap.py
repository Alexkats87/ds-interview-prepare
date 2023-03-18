"""
Min Heap implementation
"""


class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    @staticmethod
    def parent_idx(idx):
        return idx // 2

    @staticmethod
    def left_child_idx(idx):
        return idx * 2

    @staticmethod
    def right_child_idx(idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min_ = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return min_

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    def heapify_up(self):
        idx = self.count
        swap_count = 0
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                swap_count += 1
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)

        element_count = len(self.heap_list)
        if element_count > 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
        print("Heap Restored")

    def heapify_down(self):
        idx = 1
        # starts at 1 because we swapped first and last elements
        swap_count = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                swap_count += 1
                tmp = self.heap_list[smaller_child_idx]
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = smaller_child_idx

        element_count = len(self.heap_list)
        if element_count >= 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
        print("Heap Restored")

    def print_heap(self):
        print(self.heap_list)


if __name__ == "__main__":

    h = MinHeap()
    h.add(1)
    h.add(2)
    h.add(3)
    h.add(4)
    h.add(5)
    h.add(6)
    h.add(7)

    h.print_heap()
    print(h.parent_idx(6))
    print(h.parent_idx(7))

