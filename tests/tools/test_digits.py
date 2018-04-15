from tools.digits import get_digits, sum_digits
import unittest


class TestGetDigits(unittest.TestCase):

    def test_simple(self):
        iter = get_digits(12)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, lambda: next(iter))

        iter = get_digits(999)
        self.assertEqual(next(iter), 9)
        self.assertEqual(next(iter), 9)
        self.assertEqual(next(iter), 9)
        self.assertRaises(StopIteration, lambda: next(iter))


class TestSumDigits(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_digits(12), 3)
        self.assertEqual(sum_digits(999), 27)

    def test_power(self):
        self.assertEqual(sum_digits(1634, p=4), 1634)
        self.assertEqual(sum_digits(8208, p=4), 8208)
