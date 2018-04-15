from solutions.level2.problem28 import number_spiral_diags
import unittest


class TestProblem28(unittest.TestCase):

    def test_example(self):
        self.assertEqual(number_spiral_diags(5), 101)

    def test_problem(self):
        self.assertEqual(number_spiral_diags(1001), 669171001)
