from tools.digit_sum import digit_sum
import unittest

class TestCollatzNext(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(digit_sum(12), 3)
        self.assertEqual(digit_sum(999), 27)
