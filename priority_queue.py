import sys


class Process:
    def __init__(self, key, value):
        """Initialize a process with priority 'key' and value 'value'.

        It represents the jobs/processes in a shared computer with certain
        priority associated with it. The value represents certain attribute
        associated with the job/process.
        """
        self.key = key
        self.value = value


class MaxPriorityQueue():
    """Implementation of maximum priority queue using binary heap."""

    def __init__(self):
        """Initialize an instance of maximum priority queue."""
        self.__heap = list()
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
        if l <= self.__size and self.__heap[l].key > self.__heap[index].key:
            largest = l
        else:
            largest = index
        if r <= self.__size and self.__heap[r].key > self.__heap[largest].key:
            largest = r
        if largest != index:
            # Exchange the node with its largest child and recursively move down to maintain max-heap property
            self.__heap[index], self.__heap[largest] = self.__heap[largest], self.__heap[index]
            self.__max_heapify(largest)

    @property
    def priority_queue(self):
        """Return the heap (list) associated with the priority queue."""
        return list(map(lambda x: x.key, self.__heap))

    # Max Priority Queue Methods

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
        self.__heap.append(process)
        self.increase_key(self.__size-1, key)

    def maximum(self):
        """Return the element with the maximum priority (or the largest key)."""
        if self.__size < 1:
            # ERROR: Heap underflow!
            return False
        return self.__heap[0].key

    def extract_max(self):
        """Remove and return the element with the maximum priority (or the largest key)."""
        if self.__size < 1:
            # ERROR: Heap underflow!
            return False
        max_element = self.__heap[0]
        self.__heap[0] = self.__heap[self.__size-1]
        self.__size -= 1
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
        if key < self.__heap[index].key:
            # ERROR: New key is smaller than the current key!
            return False
        self.__heap[index].key = key
        while index > 0 and self.__heap[self.__parent(index)].key < self.__heap[index].key:
            # Exchange the element with its parent
            self.__heap[index], self.__heap[self.__parent(index)] = self.__heap[self.__parent(index)], self.__heap[index]
            index = self.__parent(index)
