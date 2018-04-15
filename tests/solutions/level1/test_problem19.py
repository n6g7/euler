from solutions.level1.problem19 import count_sundays
import unittest


class TestProblem19(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(count_sundays(100), 171)
