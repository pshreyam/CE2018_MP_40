import unittest

from priority_queue import MaxPriorityQueue


class TestMaxPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.mpq = MaxPriorityQueue()

    def test_insert(self):
        self.mpq.insert(10)
        self.assertListEqual(self.mpq.priority_queue, [10])
        self.mpq.insert(2)
        self.assertListEqual(self.mpq.priority_queue, [10, 2])
        self.mpq.insert(20)
        self.assertListEqual(self.mpq.priority_queue, [20, 2, 10])
        self.mpq.insert(30)
        self.assertListEqual(self.mpq.priority_queue, [30, 20, 10, 2])
        self.mpq.insert(15)
        self.assertListEqual(self.mpq.priority_queue, [30, 20, 10, 2, 15])

    def test_maximum(self):
        self.mpq.insert(10)
        self.assertEqual(self.mpq.maximum(), 10)
        self.mpq.insert(2)
        self.assertEqual(self.mpq.maximum(), 10)
        self.mpq.insert(20)
        self.assertEqual(self.mpq.maximum(), 20)
        self.mpq.insert(30)
        self.assertEqual(self.mpq.maximum(), 30)
        self.mpq.insert(15)
        self.assertEqual(self.mpq.maximum(), 30)

    def test_extract_max(self):
        pass

    def test_increase_key(self):
        pass
