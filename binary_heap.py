import unittest

from math import floor
from random import randint


class BinHeap(object):
    def __init__(self, comparator=lambda x, y: x > y):
        self.comparator = comparator
        self.data = []

    def parent_id(self, i):
        return int(floor((i-1)/2))

    def parent(self, i):
        return self.data[self.parent_id(i)]

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def insert(self, v):
        self.data.append(v)
        last_i = len(self.data) - 1
        if last_i == 0:
            return
        parent_id = self.parent_id(last_i)

        while (not self.comparator(self.parent(last_i), v)) and last_i != 0:

            self.swap(last_i, parent_id)
            last_i = parent_id
            parent_id = self.parent_id(last_i)

    def empty(self):
        return self.data == []

    def extract(self):
        if self.empty():
            return None

        ret = self.data[0]

        if len(self.data) == 1:
            self.data = []
            return ret

        self.data[0] = self.data[-1]
        self.data = self.data[0:-1]

        left = 1
        right = 2
        largest = 0
        prev = -1

        while largest != prev:
            prev = largest
            if left < len(self.data) and
            self.comparator(self.data[left], self.data[largest]):
                largest = left

            if right < len(self.data) and
            self.comparator(self.data[right], self.data[largest]):
                largest = right

            self.swap(largest, prev)
            left = largest*2 + 1
            right = largest*2 + 2
        return ret


class TestPQ(unittest.TestCase):
    def test_push_increasingly(self):
        b = BinHeap()
        for i in xrange(1, 50):
            b.insert(i)

        for i in xrange(49, 0, -1):
            self.assertEqual(b.extract(), i)

    def test_push_decreasingly(self):
        b = BinHeap()
        for i in xrange(50, 1, -1):
            b.insert(i)

        for i in xrange(50, 1, -1):
            self.assertEqual(b.extract(), i)

    def test_min_heap(self):
        b = BinHeap(comparator=lambda x, y: x < y)

        for i in xrange(50, 0, -1):
            b.insert(i)

        for i in xrange(1, 50):
            self.assertEqual(b.extract(), i)

    def test_push_randomly(self):
        data = []
        b = BinHeap()

        for i in xrange(0, 100):
            r = randint(0, 100)
            b.insert(r)
            data.append(r)

        data.sort()
        data.reverse()

        for i in data:
            self.assertEqual(b.extract(), i)

    def test_edge_cases(self):
        b = BinHeap()
        self.assertEqual(b.extract(), None)
        b.insert(1)
        self.assertEqual(b.extract(), 1)
        self.assertEqual(b.extract(), None)


if __name__ == '__main__':
    unittest.main()
