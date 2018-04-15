from solutions.level2.problem27 import quadratic_primes
import unittest


class TestProblem27(unittest.TestCase):

    def test_example(self):
        self.assertEqual(quadratic_primes(50), -235)

    def test_problem(self):
        self.assertEqual(quadratic_primes(1000), -59231)
