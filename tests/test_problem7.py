from problem7 import nth_prime
import unittest

class TestProblem7(unittest.TestCase):

    def test_example(self):
        self.assertEqual(nth_prime(6), 13)

    def test_problem(self):
        self.assertEqual(nth_prime(10001), 104743)
