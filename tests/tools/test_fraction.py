from tools.fraction import decimal_expansion, recurring_cycle
import unittest


class TestDecimalExpansion(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(decimal_expansion(1), (0, 0))
        self.assertEqual(decimal_expansion(2), (1, 0))
        self.assertEqual(decimal_expansion(3), (0, 1))
        self.assertEqual(decimal_expansion(4), (2, 0))
        self.assertEqual(decimal_expansion(5), (1, 0))
        self.assertEqual(decimal_expansion(6), (1, 1))
        self.assertEqual(decimal_expansion(7), (0, 6))
        self.assertEqual(decimal_expansion(8), (3, 0))
        self.assertEqual(decimal_expansion(9), (0, 1))
        self.assertEqual(decimal_expansion(10), (1, 0))


class TestRecurringCycle(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(recurring_cycle(2), 0)
        self.assertEqual(recurring_cycle(3), 1)
        self.assertEqual(recurring_cycle(6), 1)
        self.assertEqual(recurring_cycle(7), 6)
