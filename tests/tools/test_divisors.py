from tools.divisors import count_divisors, get_divisors, sum_divisors
import unittest

class TestCountDivisors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_divisors(1), 1)
        self.assertEqual(count_divisors(2), 2)
        self.assertEqual(count_divisors(3), 2)
        self.assertEqual(count_divisors(4), 3)
        self.assertEqual(count_divisors(5), 2)
        self.assertEqual(count_divisors(18), 6)

class TestGetDivisors(unittest.TestCase):

    def test_simple(self):
        iter = get_divisors(12)

        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 4)
        self.assertEqual(next(iter), 6)

class TestSumDivisors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_divisors(220), 284)
        self.assertEqual(sum_divisors(284), 220)
