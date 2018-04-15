from solutions.level2.problem37 import truncatable_primes
import unittest


class TestProblem37(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(truncatable_primes(11), 748317)
