class _DoublyLinkedBase:
    """A base class providing doubly linked list representation"""

    # -------------------Non-Public _Node class-------------------
    class _Node:
        """A lightweight class representing a single node of the Doubly linked list"""
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    # --------------------Empty Exception--------------------------
    class Empty(Exception):
        pass

    # -------------------Private DLB methods-----------------------
    def __init__(self):
        """Creates an empty Doubly linked list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._n = 0
        self._header._next = self._trailer
        self._trailer._prev = self._header

    def __len__(self):
        """Returns the lenth of the list"""
        return self._n

    # -------------------Public DLB methods-----------------------
    def is_empty(self):
        """Returns True if the list is empty"""
        return self._n == 0

    def _delete_node(self, node):
        """Removes and returns the specified node from the list"""
        node._prev._next = node._next
        node._next._prev = node._prev

        self._n -= 1
        element = node._element
        node._next = node._prev = node._element = None
        return element

    def _insert_between(self, element, predecessor, successor):
        new_node = self._Node(element, successor, predecessor)
        predecessor._next = new_node
        successor._prev = new_node

        self._n += 1
        return new_node


class Deque(_DoublyLinkedBase):
    """A Double Ended Queue implementation using a doubly linked list"""

    def first(self):
        if self.is_empty():
            raise self.Empty("The deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise self.Empty("The deque is empty")
        return self._trailer._prev._element

    def insert_left(self, element):
        """Inserts a node to the beginning of the deque"""
        self._insert_between(element, self._header, self._header._next)

    def insert_right(self, element):
        """Inserts a node to the end of the deque"""
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_leftmost(self):
        """Removes and returns the first node of the deque.\n
        Raises Empty Exception if deque is empty"""
        if self.is_empty():
            raise self.Empty("The deque is empty")

        return self._delete_node(self._header._next)

    def delete_rightmost(self):
        """Removes and returns the last node of the deque.\n
        Raises Empty Exception if deque is empty"""
        if self.is_empty():
            raise self.Empty("The deque is empty")

        return self._delete_node(self._trailer._prev)


if __name__ == "__main__":
    deque = Deque()

    print('Case 1: Loading data . . .')
    for i in range(0, 8):
        if i <= 3:
            deque.insert_left(i)
            deque.insert_right(i)
        if i > 3:
            deque.insert_right(i)

    print('Case 1: Deleting from the beginning of the deque')
    while not deque.is_empty():
        print(deque.delete_leftmost())

    print('Case 2: Loading data . . .')
    for i in range(0, 8):
        if i <= 3:
            deque.insert_left(i)
            deque.insert_right(i)
        if i > 3:
            deque.insert_right(i)
    print('Case 2: Deleting from the ending of the deque')
    while not deque.is_empty():
        print(deque.delete_rightmost())
