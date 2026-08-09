from solutions.level1.problem9 import brute
import unittest


class TestProblem9(unittest.TestCase):

    def test_example(self):
        self.assertEqual(brute(12), 60)
