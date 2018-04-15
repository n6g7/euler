from solutions.level1.problem12 import triangle_numbers_divisors
import unittest


class TestProblem12(unittest.TestCase):

    def test_example(self):
        self.assertEqual(triangle_numbers_divisors(5), 28)

    def test_problem(self):
        self.assertEqual(triangle_numbers_divisors(500), 76576500)
