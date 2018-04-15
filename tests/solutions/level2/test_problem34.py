from solutions.level2.problem34 import digit_factorials
import unittest


class TestProblem34(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(digit_factorials(100000), 40730)
