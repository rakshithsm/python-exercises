class CircularQueue:
    """Queue implementation using circularly linked list"""

    # -----------------------Nested Node Class--------------------------------
    class _Node:
        """A lightweight class for storing a singly linked node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            """Creates a node for the element with a reference to the next node"""
            self._element = element
            self._next = next

    # -----------------------Nested EmptyException Class-----------------------
    class Empty(Exception):
        pass

    # -----------------------Stack Methods-------------------------------------
    def __init__(self):
        """Initializes an empty circular queue"""
        self._n = 0
        self._tail = None

    def __len__(self):
        """Returns the length of the circular queue"""
        return self._n

    def is_empty(self):
        """Returns True if the circular queue is empty i.e _n = 0"""
        return self._n == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.\n
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty( 'Queue is empty' )
        head = self. tail. next
        return head. element

    def enqueue(self, element):
        """Adds the node containing element in between the tail and head and makes this element as the new tail"""
        # new_node = self._Node(element, None)

        # if self.is_empty():
        #     self._tail = new_node
        # else:
        #     new_node._next = self._tail._next

        # self._tail._next = new_node
        # self._n += 1

        new_node = self._Node(element, None) # node will be new tail node
        if self.is_empty( ):
            new_node._next = new_node # initialize circularly
        else:
            new_node._next = self._tail._next # new node points to head
            self._tail._next = new_node # old tail points to new node
        self._tail = new_node # new node becomes the tail
        self._n += 1

    def dequeue(self):
        """Removes and returns the First element of the circular queue.\n
        Raises an Empty exception if queue is empty."""
        if self.is_empty():
            raise self.Empty("The circular queue is empty.")

        old_head = self._tail._next

        if self._n == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next

        self._n -= 1

        return old_head._element

    def rotate(self):
        """Moves the node at the begining of the queue to the end"""
        if self._n > 0:
            self._tail = self._tail._next


if __name__ == '__main__':
    circular_queue = CircularQueue()
    
    print('Case 1: Loading to queue.....')
    for i in range(10):
        circular_queue.enqueue(i)

    print('Case 1: Unloading from queue completely.....')
    while not circular_queue.is_empty():
        print(circular_queue.dequeue())

    print('Case 2: Loading to queue.....')
    for i in range(10):
        circular_queue.enqueue(i)

    print('Case 2: Rotating once')
    circular_queue.rotate()

    print('Case 2: Unloading from queue completely.....')
    while not circular_queue.is_empty():
        print(circular_queue.dequeue())