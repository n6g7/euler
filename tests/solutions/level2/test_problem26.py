from solutions.level2.problem26 import longest_recurring_cycle
import unittest

class TestProblem26(unittest.TestCase):

    def test_example(self):
        self.assertEqual(longest_recurring_cycle(10), 7)

    def test_problem(self):
        self.assertEqual(longest_recurring_cycle(1000), 983)
