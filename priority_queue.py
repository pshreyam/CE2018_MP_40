import sys


class Process:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MaxPriorityQueue():
    """Implementation of maximum priority queue using binary heap."""

    def __init__(self):
        """Initialize an instance of maximum priority queue."""
        self.heap = list()
        self.__size = 0

    def __parent(self, index):
        """Return the index of the parent."""
        return (index - 1) // 2

    def __left_child(self, index):
        """Return the index of the left child."""
        return 2 * index + 1

    def __right_child(self, index):
        """Return the index of the right child."""
        return 2 * index + 2

    def __max_heapify(self, index):
        """Maintain the max-heap property by swapping with the largest child in
        case the max-heap property is violated."""
        l = self.__left_child(index)
        r = self.__right_child(index)
        if l <= self.__size and self.heap[l].key > self.heap[index].key:
            largest = l
        else:
            largest = index
        if r <= self.__size and self.heap[r].key > self.heap[largest].key:
            largest = r
        if largest != index:
            # Exchange the node with its largest child and recursively move down to maintain max-heap property
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.__max_heapify(largest)

    @property
    def priority_queue(self):
        return list(map(lambda x: x.key, self.heap))

    def insert(self, key, value):
        """Insert new element in the priority queue.

        Args:
            key
                The priority of the element to be inserted.
            value
                The value of the element to be inserted.
        """
        self.__size += 1
        # Set the last element's priority to a very small number initially
        process = Process(-sys.maxsize, value)
        self.heap.append(process)
        self.increase_key(self.__size-1, key)

    def maximum(self):
        """Return the element with the maximum priority (or the largest key)."""
        if self.__size < 1:
            print("Heap underflow!")
            return -1
        return self.heap[0].key

    def extract_max(self):
        """Remove and return the element with the maximum priority (or the largest key)."""
        if self.__size < 1:
            print("Heap underflow!")
            return -1
        max_element = self.heap[0]
        self.heap[0] = self.heap[self.__size-1]
        self.__max_heapify(0)
        return max_element.key

    def increase_key(self, index, key):
        """Increase the value of element in position 'index' to new value key.

        Args:
            index
                The index of the element whose priority has to be increased.
            key
                The new priority for the element in position 'index'.
        """
        if key < self.heap[index].key:
            print("New key is smaller than the current key!")
        self.heap[index].key = key
        while index > 0 and self.heap[self.__parent(index)].key < self.heap[index].key:
            # Exchange the element with its parent
            self.heap[index], self.heap[self.__parent(index)] = self.heap[self.__parent(index)], self.heap[index]
            index = self.__parent(index)


if __name__ == "__main__":
    mpq = MaxPriorityQueue()

    mpq.insert(10, "Value for 10")
    mpq.insert(2, "Value for 2")
    mpq.insert(20, "Value for 20")
    # mpq.insert(30)
    # mpq.insert(15)
    print(mpq.priority_queue)
