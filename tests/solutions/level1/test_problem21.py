from solutions.level1.problem21 import sum_amicables
import unittest


class TestProblem21(unittest.TestCase):

    def test_example(self):
        self.assertEqual(sum_amicables(1000), 504)

    def test_problem(self):
        self.assertEqual(sum_amicables(10000), 31626)
