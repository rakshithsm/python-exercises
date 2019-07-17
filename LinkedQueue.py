class LinkedQueue:
    """FIFO queue implementation using linked list."""

    # -----------------------Nested Node Class--------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # -----------------------Nested EmptyException Class-----------------------
    class Empty(Exception):
        pass

    # -----------------------Stack Methods-------------------------------------
    def __init__(self):
        """create an empty queue."""
        self._n = 0
        self._head = None
        self._tail = None

    def __len__(self):
        """Returns the length of the queue."""
        return self._n

    def is_empty(self):
        """Returns True if the length of queue is 0 i.e queue is empty."""
        return self._n == 0

    def first(self):
        """Returns the first element of the queue
         without removing it from the queue"""
        return self._head._element

    def dequeue(self):
        """Removes and returns the first element of the queue."""
        if self.is_empty():
            raise self.Empty("The queue is empty.")

        oldHead = self._head
        newHead = self._head._next
        self._head = newHead
        self._n -= 1
        return oldHead._element

    def enqueue(self, element):
        newNode = self._Node(element, None)

        if self.is_empty():
            self._head = newNode
        else:
            self._tail._next = newNode

        self._n += 1
        self._tail = newNode


if __name__ == '__main__':
    queue = LinkedQueue()
    print('Case 1: Loading 10 elements to the queue ....')
    for i in range(10):
        queue.enqueue(i)

    print('Case 1: Dequeing ....')
    while not queue.is_empty():
        print(queue.dequeue())

    print('Case 2: Enqueueing after a dequeue 5 elements ....')
    for i in range(5):
        queue.enqueue(i)

    print('Case 2: Dequeing ....')
    while not queue.is_empty():
        print(queue.dequeue())

    print('Case 3: Dequeing empty queue ....')
    queue.dequeue()