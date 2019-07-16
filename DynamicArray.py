import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def get_element(self, i):
        if 0 > i > self._capacity:
            raise IndexError("Error: Index out of range")
        return self._A[i]

    def append(self, element):
        if self._n == self._capacity:
            self._resize(2*self._capacity)

        self._A[self._n] = element
        self._n += 1

    def _resize(self, c):

        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def __len__(self):
        return self._n

    def insert_at(self, element, index):
        if self._n == self._capacity:
            self._resize(2*self._capacity)

        for i in range(self._n, index, -1):
            self._A[i] = self._A[i-1]

        self._A[index] = element

        self._n += 1

    def remove_from(self, index):

        for i in range(index, self._n):
            self._A[i] = self._A[i+1]

        if self._n == self._capacity/2:
            self._resize(self._capacity/2)

        self._n -= 1

    def print_array(self):
        for i in range(self._n):
            print(self.get_element(i))


if __name__ == "__main__":
    a = DynamicArray()
    a.append(0)
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    a.append(8)
    a.append(9)
    a.append(10)
    # print(a.get_element(0))
    print(a.insert_at(100, 1))
    a.print_array()
    print(a.remove_from( 1))
    a.print_array()
