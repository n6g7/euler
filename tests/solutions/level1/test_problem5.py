from solutions.level1.problem5 import smallest_multiple
import unittest

class TestProblem5(unittest.TestCase):

    def test_example(self):
        self.assertEqual(smallest_multiple(10), 2520)

    def test_problem(self):
        self.assertEqual(smallest_multiple(20), 232792560)
