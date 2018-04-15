from solutions.level1.problem25 import n_digit_fib
import unittest


class TestProblem25(unittest.TestCase):

    def test_example(self):
        self.assertEqual(n_digit_fib(3), 12)

    def test_problem(self):
        self.assertEqual(n_digit_fib(1000), 4782)
