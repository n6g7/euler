from tools.divisors import count_divisors
import unittest

class TestCountDivisors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_divisors(1), 1)
        self.assertEqual(count_divisors(2), 2)
        self.assertEqual(count_divisors(3), 2)
        self.assertEqual(count_divisors(4), 3)
        self.assertEqual(count_divisors(5), 2)
        self.assertEqual(count_divisors(18), 6)
