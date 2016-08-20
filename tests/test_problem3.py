from problem3 import largest_prime_factor
import unittest

class TestProblem3(unittest.TestCase):

    def test_example(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_problem(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)
