class LinkedStack:
    """LIFO stack implementation using linked lists for storage."""

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
        """Create an empty stack"""
        self._n = 0
        self._head = None

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._n

    def is_empty(self):
        """Return TRUE if stack has no elements"""
        return self._n == 0

    def push(self, element):
        """Inserts a node to the top of the stack"""
        self._head = self._Node(element, self._head)
        self._n += 1

    def peek_top(self):
        """Returns the top node of the stack without removing it"""
        if self.is_empty():
            raise self.Empty("The stack is empty")
        return self._head._element

    def pop(self):
        """Removes and returns the top node of the stack"""
        if self.is_empty():
            raise self.Empty("The stack is empty")
        oldHead = self._head
        self._head = self._head._next
        self._n -= 1
        return oldHead._element


if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    while not stack.is_empty():
        print(stack.pop())
