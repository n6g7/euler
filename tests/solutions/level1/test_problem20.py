from solutions.level1.problem20 import factorial_digit_sum
import unittest

class TestProblem20(unittest.TestCase):

    def test_example(self):
        self.assertEqual(factorial_digit_sum(10), 27)

    def test_problem(self):
        self.assertEqual(factorial_digit_sum(100), 648)
