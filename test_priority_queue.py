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
        mpq_for_insertion.insert(5, "Value for 5")
        self.assertListEqual(mpq_for_insertion.priority_queue, [5])
        mpq_for_insertion.insert(6, "Value for 6")
        self.assertListEqual(mpq_for_insertion.priority_queue, [6, 5])
        mpq_for_insertion.insert(10, "Value for 10")
        self.assertListEqual(mpq_for_insertion.priority_queue, [10, 5, 6])
        mpq_for_insertion.insert(4, "Value for 4")
        # No change since 4 < 5
        self.assertListEqual(mpq_for_insertion.priority_queue, [10, 5, 6, 4])
        mpq_for_insertion.insert(7, "Value for 7")
        self.assertListEqual(mpq_for_insertion.priority_queue, [10, 7, 6, 4, 5])

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
        self.assertTupleEqual(self.mpq.maximum(), (30, "Value for 30"))
        # Less than the smallest key in the priority queue
        self.mpq.insert(1, "Value for 1")
        self.assertTupleEqual(self.mpq.maximum(), (30, "Value for 30"))
        # Intermediate key between the min and max key
        self.mpq.insert(5, "Value for 5")
        self.assertTupleEqual(self.mpq.maximum(), (30, "Value for 30"))
        # Greater than the largest key in the priority queue
        self.mpq.insert(70, "Value for 70")
        self.assertTupleEqual(self.mpq.maximum(), (70, "Value for 70"))

        # New empty priority queue for Heap Underflow case
        mpq_for_maximum = MaxPriorityQueue()
        self.assertEqual(mpq_for_maximum.maximum(), False)

    def test_extract_max(self):
        self.assertTupleEqual(self.mpq.extract_max(), (30, "Value for 30"))
        self.assertListEqual(self.mpq.priority_queue, [20, 15, 10, 2])
        self.assertTupleEqual(self.mpq.extract_max(), (20, "Value for 20"))
        self.assertListEqual(self.mpq.priority_queue, [15, 2, 10])
        self.assertTupleEqual(self.mpq.extract_max(), (15, "Value for 15"))
        self.assertListEqual(self.mpq.priority_queue, [10, 2])
        self.assertTupleEqual(self.mpq.extract_max(), (10, "Value for 10"))
        self.assertListEqual(self.mpq.priority_queue, [2])
        self.assertTupleEqual(self.mpq.extract_max(), (2, "Value for 2"))
        self.assertListEqual(self.mpq.priority_queue, [])
        # Heap underflow
        self.assertEqual(self.mpq.extract_max(), False)
