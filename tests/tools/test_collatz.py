from tools.collatz import collatz_next, collatz_length
import unittest

class TestCollatzNext(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(collatz_next(1), 4)
        self.assertEqual(collatz_next(2), 1)
        self.assertEqual(collatz_next(3), 10)
        self.assertEqual(collatz_next(4), 2)
        self.assertEqual(collatz_next(5), 16)
        self.assertEqual(collatz_next(18), 9)

class TestCollatzLength(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(collatz_length(1), 1)
        self.assertEqual(collatz_length(2), 2)
        self.assertEqual(collatz_length(3), 8)
        self.assertEqual(collatz_length(4), 3)
        self.assertEqual(collatz_length(5), 6)
