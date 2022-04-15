import unittest

from priority_queue import MaxPriorityQueue


class TestMaxPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.mpq = MaxPriorityQueue()
        self.mpq.insert(10, "Value for 10")
        self.mpq.insert(2, "Value for 2")
        self.mpq.insert(20, "Value for 20")
        self.mpq.insert(30, "Value for 30")
        self.mpq.insert(15, "Value for 15")

    def test_insert(self):
        mpq_for_insertion = MaxPriorityQueue()
        mpq_for_insertion.insert(10, "Value for 10")
        self.assertListEqual(mpq_for_insertion.priority_queue, [10])
        mpq_for_insertion.insert(2, "Value for 2")
        self.assertListEqual(mpq_for_insertion.priority_queue, [10, 2])
        mpq_for_insertion.insert(20, "Value for 20")
        self.assertListEqual(mpq_for_insertion.priority_queue, [20, 2, 10])
        mpq_for_insertion.insert(30, "Value for 30")
        self.assertListEqual(mpq_for_insertion.priority_queue, [30, 20, 10, 2])
        mpq_for_insertion.insert(15, "Value for 15")
        self.assertListEqual(mpq_for_insertion.priority_queue, [30, 20, 10, 2, 15])

    def test_increase_key(self):
        # Initially: [30, 20, 10, 2, 15]
        self.mpq.increase_key(4, 40)
        # Before heapify: [30, 20, 10, 2, 40]
        # Expected (After heapify): [40, 30, 10, 2, 20]
        self.assertListEqual(self.mpq.priority_queue, [40, 30, 10, 2, 20])
        self.mpq.increase_key(2, 50)
        # Before heapify: [40, 30, 50, 2, 20]
        # Expected (After heapify): [50, 30, 40, 2, 20]
        self.assertListEqual(self.mpq.priority_queue, [50, 30, 40, 2, 20])
        # Key in index 2 (30) is greater than key provided (10)
        self.assertEqual(self.mpq.increase_key(2, 10), False)

    def test_maximum(self):
        self.assertEqual(self.mpq.maximum(), 30)
        # Less than the smallest key in the priority queue
        self.mpq.insert(1, "Value for 1")
        self.assertEqual(self.mpq.maximum(), 30)
        # Intermediate key between the min and max key
        self.mpq.insert(5, "Value for 5")
        self.assertEqual(self.mpq.maximum(), 30)
        # Greater than the largest key in the priority queue
        self.mpq.insert(70, "Value for 70")
        self.assertEqual(self.mpq.maximum(), 70)

        # New empty priority queue
        mpq_for_maximum = MaxPriorityQueue()
        self.assertEqual(mpq_for_maximum.maximum(), False)

    def test_extract_max(self):
        self.assertEqual(self.mpq.extract_max(), 30)
        self.assertEqual(self.mpq.extract_max(), 20)
        self.assertEqual(self.mpq.extract_max(), 15)
        self.assertEqual(self.mpq.extract_max(), 10)
        self.assertEqual(self.mpq.extract_max(), 2)
        # Heap underflow
        self.assertEqual(self.mpq.extract_max(), False)
