from solutions.level2.problem35 import circular_primes
import unittest


class TestProblem35(unittest.TestCase):

    def test_example(self):
        self.assertEqual(circular_primes(100), 13)

    def test_problem(self):
        self.assertEqual(circular_primes(1000000), 55)
