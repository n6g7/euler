from solutions.level1.problem10 import sum_primes
import unittest


class TestProblem10(unittest.TestCase):

    def test_example(self):
        self.assertEqual(sum_primes(10), 17)
