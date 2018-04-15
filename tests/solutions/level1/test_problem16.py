from solutions.level1.problem16 import power_digit_sum
import unittest


class TestProblem16(unittest.TestCase):

    def test_example(self):
        self.assertEqual(power_digit_sum(15), 26)

    def test_problem(self):
        self.assertEqual(power_digit_sum(1000), 1366)
