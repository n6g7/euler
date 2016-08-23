from solutions.level1.problem14 import longest_collatz_sequence
import unittest

class TestProblem14(unittest.TestCase):

    def test_example(self):
        self.assertEqual(longest_collatz_sequence(10), 9)

    def test_problem(self):
        self.assertEqual(longest_collatz_sequence(1000000), 837799)
