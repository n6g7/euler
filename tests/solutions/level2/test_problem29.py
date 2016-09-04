from solutions.level2.problem29 import distinct_powers
import unittest

class TestProblem29(unittest.TestCase):

    def test_example(self):
        self.assertEqual(distinct_powers(5), 15)

    def test_problem(self):
        self.assertEqual(distinct_powers(100), 9183)
