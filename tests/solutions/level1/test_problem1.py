from solutions.level1.problem1 import sum_multiples
import unittest

class TestProblem1(unittest.TestCase):

    def test_example(self):
        self.assertEqual(sum_multiples(10), 23)

    def test_problem(self):
        self.assertEqual(sum_multiples(1000), 233168)
