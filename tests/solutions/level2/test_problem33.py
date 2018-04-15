from solutions.level2.problem33 import curious_fractions
import unittest


class TestProblem33(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(curious_fractions(10, 100), 100)
