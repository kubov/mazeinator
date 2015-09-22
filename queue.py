import unittest
from stack import Stack


class Queue(object):
    def __init__(self):
        self.q1 = Stack()
        self.q2 = Stack()

    def enqueue(self, v):
        self.q1.push(v)

    def empty(self):
        return self.q1.empty() and self.q2.empty()

    def dequeue(self):
        if self.q2.empty():
            if self.q1.empty():
                return None

            while not self.q1.empty():
                self.q2.push(self.q1.poptop())

        return self.q2.poptop()


class TestQueue(unittest.TestCase):
    def test_e2e(self):
        q = Queue()

        self.assertTrue(q.empty())

        q.enqueue(1)

        self.assertFalse(q.empty())

        self.assertEqual(q.dequeue(), 1)
        self.assertTrue(q.empty())

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        self.assertTrue(q.empty())


if __name__ == '__main__':
    unittest.main()
