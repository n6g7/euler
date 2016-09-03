from solutions.level1.problem24 import nth_lexicographic_permutation
import unittest

class TestProblem24(unittest.TestCase):

    def test_example(self):
        self.assertEqual(nth_lexicographic_permutation([0,1,2], 3), 120)

    def test_problem(self):
        self.assertEqual(nth_lexicographic_permutation([n for n in range(10)], 999999), 2783915460)
